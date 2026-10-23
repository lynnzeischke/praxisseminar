#!/usr/bin/env python3
"""Ergänzender, wiederholbarer Prüfer für die NotebookLM-Chatbelege.

Zweck (für Anhang B4 der Hausarbeit): unabhängig von NotebookLMs eigener
Selbstbewertung nachrechnen,
  (1) welchen SHA-256-Hash jede der 21 exportierten Chatdateien hat,
  (2) ob das in den Chats N19/N20/N21 eingebettete JSON byteidentisch mit
      dem jeweils separat archivierten R5-/R6-/R6.1-Output übereinstimmt,
  (3) ob die 18 normalisierten Item-Endtexte aus diesem JSON im
      Teilnehmerfragebogen-Abschnitt (B5) und im Herkunftsregister-Abschnitt
      (B2) des jeweiligen Chats tatsächlich vorkommen.

WICHTIG (Aussagegrenze, siehe Hausarbeit Anhang B4): Dieses Skript prüft
Textpräsenz nach Normalisierung und JSON-Gleichheit. Es prüft NICHT
semantische Quellenäquivalenz, Übersetzungstreue oder psychometrische
Validität. Ein PASS hier ist kein Wissenschaftlichkeitsnachweis.

Aufruf:
    python3 Nachweise/check_chat_evidence.py \
        --chats notebooklm-chatverlauf \
        --archiv notebooklm_tests \
        --out Chatbelege_Pruefergebnisse.json
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

# N-Nummerierung und R-Zuordnung wie in Anhang B1/B2 der Hausarbeit dokumentiert.
CHAT_FILES = [
    ("N01", "Design-Science-Framework.md"),
    ("N02", "Projektuebersicht_Praxisseminar.md"),
    ("N03", "Design-Audits.md"),
    ("N04", "Stresstest_01_Aufgabenkontext.md"),
    ("N05", "Stresstest_02_Firmenkontext.md"),
    ("N06", "Stresstest_03_Mehrfachkriterien.md"),
    ("N07", "Runmode_01-05.md"),
    ("N08", "Runmode_06.md"),
    ("N09", "Runmode_07.md"),
    ("N10", "Runmode_08.md"),
    ("N11", "Runmode_09.md"),
    ("N12", "Runmode_10.md"),
    ("N13", "Runmode_11.md"),
    ("N14", "Runmode_12.md"),
    ("N15", "Runmode_13.md"),
    ("N16", "Runmode_14.md"),
    ("N17", "Runmode_15.md"),
    ("N18", "Runmode_16.md"),
    ("N19", "Runmode_17.md"),
    ("N20", "Runmode_18.md"),
    ("N21", "Runmode_18_NOTEBOOKLM.md"),
]

# Welcher Chat enthält den Lauf gegen welche archivierte Ausgabe.
RUN_MAP = {
    "N19": ("R5", "NotebookLM_Ausgabe_R5.txt"),
    "N20": ("R6", "NotebookLM_Ausgabe_R6.txt"),
    "N21": ("R6.1", "NotebookLM_Ausgabe_R6_1.txt"),
}

JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", re.IGNORECASE)


def sha256_of(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text: str) -> str:
    """Entfernt Zitatmarker, Markdown- und Anführungszeichen; vereinheitlicht Leerraum."""
    text = re.sub(r"\[\d+\]", "", text)
    text = text.replace("**", "").replace("`", "")
    text = text.replace("„", '"').replace("“", '"').replace("”", '"')
    text = text.replace('"', "").replace("'", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_json_objects(text: str):
    return [m.group(1) for m in JSON_BLOCK_RE.finditer(text)]


def largest_valid_json(blocks):
    """Von mehreren Codeblöcken denjenigen zurückgeben, der als B7-Itemliste parsebar ist
    (enthält den Schlüssel 'items') und am meisten Items hat."""
    best = None
    for b in blocks:
        try:
            obj = json.loads(b)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and "items" in obj:
            if best is None or len(obj.get("items", [])) > len(best.get("items", [])):
                best = obj
    return best


def split_sections(markdown: str):
    """Grobe Abschnittstrennung anhand der B-Überschriften, wie in den Chat-Exporten üblich.
    Die Exporte schreiben Abschnittstitel als eigene Zeile, z. B.
    'B2 – Vollständige Item-Traceability' oder 'B5 – ... Teilnehmerfragebogen',
    nicht als Markdown-#-Überschrift."""
    sections = {}
    pattern = re.compile(r"(?m)^\s*#{0,6}\s*B([0-9])(?:\s*[–\-:.]| )")
    matches = list(pattern.finditer(markdown))
    for idx, m in enumerate(matches):
        label = f"B{m.group(1)}"
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown)
        sections.setdefault(label, "")
        sections[label] += markdown[start:end]
    return sections


def presence_check(items, section_text):
    norm_section = normalize(section_text)
    found = 0
    missing = []
    for it in items:
        qt = it.get("question_text") or it.get("item_text") or ""
        norm_qt = normalize(qt)
        if norm_qt and norm_qt in norm_section:
            found += 1
        else:
            missing.append(it.get("item_id", "?"))
    return found, missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chats", default="notebooklm-chatverlauf")
    ap.add_argument("--archiv", default="notebooklm_tests")
    ap.add_argument("--out", default="Chatbelege_Pruefergebnisse.json")
    args = ap.parse_args()

    chats_dir = pathlib.Path(args.chats)
    archiv_dir = pathlib.Path(args.archiv)

    report = {"dateien": [], "testlaeufe": {}, "hinweis": (
        "Prueft Textpraesenz nach Normalisierung und JSON-Gleichheit. "
        "Kein Nachweis semantischer Quellenaequivalenz, Uebersetzungstreue "
        "oder psychometrischer Validitaet."
    )}

    for n_id, fname in CHAT_FILES:
        fpath = chats_dir / fname
        if not fpath.exists():
            report["dateien"].append({"id": n_id, "datei": fname, "status": "FEHLT"})
            continue
        h = sha256_of(fpath)
        report["dateien"].append({
            "id": n_id, "datei": fname, "sha256": h, "bytes": fpath.stat().st_size,
        })

    for n_id, (run_label, archiv_fname) in RUN_MAP.items():
        chat_fname = dict(CHAT_FILES)[n_id]
        chat_path = chats_dir / chat_fname
        archiv_path = archiv_dir / archiv_fname
        entry = {"chat_datei": chat_fname, "archiv_datei": archiv_fname}

        if not chat_path.exists() or not archiv_path.exists():
            entry["status"] = "DATEI_FEHLT"
            report["testlaeufe"][run_label] = entry
            continue

        chat_text = chat_path.read_text(encoding="utf-8", errors="replace")
        archiv_text = archiv_path.read_text(encoding="utf-8", errors="replace")

        chat_json = largest_valid_json(extract_json_objects(chat_text))
        archiv_json = largest_valid_json(extract_json_objects(archiv_text))

        entry["chat_json_gefunden"] = chat_json is not None
        entry["archiv_json_gefunden"] = archiv_json is not None

        if chat_json is not None and archiv_json is not None:
            entry["json_identisch"] = (chat_json == archiv_json)
            entry["chat_item_anzahl"] = len(chat_json.get("items", []))
            entry["archiv_item_anzahl"] = len(archiv_json.get("items", []))
        else:
            entry["json_identisch"] = None

        items = (chat_json or {}).get("items", [])
        sections = split_sections(chat_text)
        b2_text = sections.get("B2", "")
        b5_text = sections.get("B5", "")

        if items:
            b2_found, b2_missing = presence_check(items, b2_text)
            b5_found, b5_missing = presence_check(items, b5_text)
            entry["b2_textpraesenz"] = f"{b2_found}/{len(items)}"
            entry["b2_fehlend"] = b2_missing
            entry["b5_textpraesenz"] = f"{b5_found}/{len(items)}"
            entry["b5_fehlend"] = b5_missing
        else:
            entry["b2_textpraesenz"] = "nicht pruefbar (kein JSON mit items gefunden)"
            entry["b5_textpraesenz"] = "nicht pruefbar (kein JSON mit items gefunden)"

        report["testlaeufe"][run_label] = entry

    out_path = pathlib.Path(args.out)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Bericht geschrieben: {out_path}")
    for run_label, entry in report["testlaeufe"].items():
        print(f"{run_label}: json_identisch={entry.get('json_identisch')} "
              f"B2={entry.get('b2_textpraesenz')} B5={entry.get('b5_textpraesenz')}")


if __name__ == "__main__":
    main()

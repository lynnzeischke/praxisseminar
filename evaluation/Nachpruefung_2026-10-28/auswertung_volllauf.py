"""Auswertung der Wiederholungsläufe W1–W3 nach den Endpunkten W-K1 bis W-K4 im Vorabplan.

Aufruf im Projektstamm:
    python3 evaluation/Nachpruefung_2026-10-28/auswertung_volllauf.py

Erwartet je Lauf die unveränderte, vollständige Antwort als
evaluation/Nachpruefung_2026-10-28/antworten/W1_Antwort.txt usw.
Prüft nur Struktur, Textgleichheit und AISES-Locator; keine semantische Quellenprüfung.
"""
from collections import Counter
from pathlib import Path
import json, re, subprocess, sys, tempfile

HERE = Path(__file__).resolve().parent
REF = HERE.parent / "R6_2_Vollproduktion_2026-10-26" / "B7_extrahiert.json"
CHECK = HERE.parent / "R6_2_Vollproduktion_2026-10-26" / "check_output.py"
ref_items = {i["item_id"]: i["question_text"] for i in json.loads(REF.read_text(encoding="utf-8"))["items"]}


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r'[\*`"“”„]', "", t)).strip()


def extract_json(s):
    dec = json.JSONDecoder()
    for m in re.finditer(r"\{\s*\"metadata\"", s):
        try:
            obj, n = dec.raw_decode(s[m.start():])
            if "items" in obj:
                return obj, s[m.start():m.start() + n]
        except json.JSONDecodeError:
            continue
    return None, None


def evaluate(path):
    s = path.read_text(encoding="utf-8-sig")
    heads = Counter("B" + m[1] for m in re.finditer(r"(?m)^(?:Teil ### )?#*\s*B([0-7]) –", s))
    k1 = all(heads.get(f"B{i}") == 1 for i in range(8))
    j, raw = extract_json(s)
    k2 = k3 = k4 = False
    check_msg = "kein JSON-Block mit metadata/items gefunden"
    if j is not None:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write("```json\n" + raw + "\n```")
        res = subprocess.run([sys.executable, str(CHECK), f.name], capture_output=True, text=True)
        k2 = res.returncode == 0
        check_msg = (res.stdout + res.stderr).strip()
        got = {i["item_id"]: i.get("question_text", "") for i in j.get("items", [])}
        k3 = set(got) == set(ref_items) and all(norm(got[k]) == norm(v) for k, v in ref_items.items())
        aises = [i for i in j.get("items", []) if str(i.get("source_evidence", {}).get("source_id", "")).upper().startswith("AISES")]
        k4 = len(aises) == 3 and all("Table 3" in i["source_evidence"].get("locator", "") and
                                     "Table 2" not in i["source_evidence"].get("locator", "") for i in aises)
    return {"lauf": path.stem.split("_")[0], "W-K1_eine_Folge": k1, "W-K2_Strukturcheck": k2,
            "W-K3_Wortlaut": k3, "W-K4_AISES_Table3": k4, "summe": sum([k1, k2, k3, k4]),
            "abschnittszaehlung": dict(sorted(heads.items())), "strukturcheck": check_msg}


files = sorted((HERE / "antworten").glob("W*_Antwort.txt"))
if not files:
    raise SystemExit("Keine Dateien antworten/W*_Antwort.txt gefunden.")
results = [evaluate(f) for f in files]
(HERE / "Auswertung_Wiederholung.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
for r in results:
    print(f"{r['lauf']}: {r['summe']}/4  K1={r['W-K1_eine_Folge']} K2={r['W-K2_Strukturcheck']} "
          f"K3={r['W-K3_Wortlaut']} K4={r['W-K4_AISES_Table3']}  Abschnitte={r['abschnittszaehlung']}")
dup = sum(not r["W-K1_eine_Folge"] for r in results)
print(f"Doppelte oder unvollständige Gesamtfolge: {dup} von {len(results)} neuen Läufen "
      f"(plus 1 von 1 am 26.10.2026).")

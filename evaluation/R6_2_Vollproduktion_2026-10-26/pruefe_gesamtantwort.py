"""Reproduzierbare Struktur-/Textprüfung; keine semantische Quellenvalidierung."""
from pathlib import Path
from collections import Counter
import json,re,subprocess,sys
b=Path(__file__).resolve().parent
s=(b/'Seiteninhalt_original.txt').read_text()
a=s.index('{\n  "metadata"');j,n=json.JSONDecoder().raw_decode(s[a:])
(b/'B7_extrahiert.json').write_text(json.dumps(j,ensure_ascii=False,indent=2))
(b/'B7_fuer_Strukturcheck.md').write_text('```json\n'+s[a:a+n]+'\n```')
res=subprocess.run([sys.executable,str(b/'check_output.py'),str(b/'B7_fuer_Strukturcheck.md')],capture_output=True,text=True)
def norm(t):return re.sub(r'\s+',' ',re.sub(r'[\*`"“”„]','',t)).strip()
h=list(re.finditer(r'(?m)^(?:Teil ### )?B([0-7]) –[^\n]*',s));counts=Counter('B'+m[1] for m in h)
sections=[]
for k,m in enumerate(h):
 if m[1] in ['2','5']:
  t=s[m.end():h[k+1].start() if k+1<len(h) else len(s)]
  sections.append({'section':'B'+m[1],'text_presence':sum(norm(i['question_text']) in norm(t) for i in j['items'])})
report={'json_structure_pass':res.returncode==0,'structure_check_output':res.stdout+res.stderr,'section_counts':dict(counts),'single_complete_sequence':all(counts.get('B'+str(i))==1 for i in range(8)),'normalized_text_presence':sections,'scale_counts':dict(Counter(i['final_scale'] for i in j['items'])),'classes':dict(Counter(i['evidence_class'] for i in j['items'])),'limits':'Textpräsenz beweist weder Eindeutigkeit noch semantische oder psychometrische Güte. Quellen-Locatoren gesondert in Pruefbericht.md geprüft.'}
(b/'Automatische_Pruefung.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))

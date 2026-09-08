import requests, json, os
from datetime import datetime, timedelta

print("BS BOT START")
t=[]
depts=[("KZN Health","construction"),("Victoria Mxenge Hospital","cleaning"),("Victoria Hospital","service"),("Nkonjeni Hospital","construction"),("Public Works","construction"),("Education GP","catering"),("COJ","security"),("Eskom","electrical"),("SANRAL","construction"),("Transport","service"),("Health Limpopo","cleaning"),("Cape Town","security"),("Water & Sanitation","plumbing"),("SASSA","security"),("PRASA","construction"),("Transnet","service"),("Home Affairs","cleaning"),("SAPO","service"),("eThekwini","construction"),("Agriculture","catering"),("UP","cleaning"),("SARS","security"),("DENEL","electrical"),("COGTA","construction")]
base=datetime.now()
for i,(d,c) in enumerate(depts):
  cl=(base+timedelta(days=7+i%15)).strftime("%Y-%m-%d")
  t.append({"title":f"{c.title()} Tender {i+1} - {d}" if i>3 else ["Replace Motor/Hoist","Cleaning gutters 2026","Fire extinguisher service","Storage container Gateway clinic"][i],"dept":d,"number":f"HOH{i+300}_26_27","category":c,"type":c,"closing":cl,"value":f"R{(i+2)*150000:,}","location":d})

open('tenders.json','w',encoding='utf-8').write(json.dumps(t,indent=2))
cards=""
for x in t:
  cards+=f"<div style='background:white;border-left:4px solid #003366;padding:12px;border-radius:8px;margin-bottom:12px'><b style='color:#003366'>{x['title']}</b><br><span style='font-size:13px'>🏢 {x['dept']} | {x['number']}</span><br><span style='font-size:13px'>🏷️ {x['category']} | ⏰ {x['closing']}</span><br><div style='display:flex;gap:8px;margin-top:10px'><a href='https://wa.me/27787417326?text=LITE R50 {x['title']}' style='flex:1;padding:10px;text-align:center;border:2px solid #003366;color:#003366;text-decoration:none;font-weight:bold;border-radius:8px;font-size:12px'>🔓 LITE R50</a><a href='https://wa.me/27787417326?text=PRO R150 {x['title']}' style='flex:1;padding:10px;text-align:center;background:#ff6600;color:white;text-decoration:none;font-weight:bold;border-radius:8px;font-size:12px'>🔒 PRO R150</a></div></div>"
d=datetime.now().strftime('%d %B %Y %H:%M')
html=f"<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>BS Tenders {len(t)}</title><style>body{{font-family:Arial;background:#f4f4f4;margin:0}}.nav{{background:#003366;color:white;padding:12px;text-align:center;position:fixed;top:0;width:100%}}.nav a{{color:white;margin:0 8px;text-decoration:none;font-weight:bold}}.container{{padding:70px 12px 20px;max-width:600px;margin:auto}}.header{{background:#003366;color:white;padding:20px;border-radius:12px;text-align:center}}</style></head><body><div class='nav'><a href='/'>Home</a><a href='/tenders.html'>Tenders ({len(t)})</a></div><div class='container'><div class='header'><h2>📢 BS DAILY TENDERS</h2><p>✅ {len(t)} LIVE | {d}</p></div>{cards}</div></body></html>"
open('tenders.html','w',encoding='utf-8').write(html)
U=os.getenv('NEO_USER');P=os.getenv('NEO_PASS')
import requests as r2
for fn in ['tenders.json','tenders.html']:
  try:
    res=r2.post('https://neocities.org/api/upload',auth=(U,P),files={fn:open(fn,'rb')})
    print(fn, res.text[:200])
  except Exception as e:
    print(e)
print("DONE SAFE")

import requests, json, os
from datetime import datetime, timedelta

print("BS BOT - COMBINED GROWING DATABASE")

# 1. LOAD OLD - THIS MAKES IT GROW
old_t = []
if os.path.exists('tenders.json'):
    try:
        with open('tenders.json','r',encoding='utf-8') as f:
            old_t = json.load(f)
        print(f"OLD FOUND: {len(old_t)}")
    except:
        old_t = []

t = old_t  # START WITH OLD

# 2. GENERATE 150 NEW DAILY
depts=[("KZN Health","construction"),("Victoria Mxenge Hospital","cleaning"),("Dept of Public Works","security"),("Dept of Education","catering"),("City of Joburg","electrical")]
titles=["Replace Motor/Hoist","Cleaning gutters","Security services 24 months","Catering for schools","Electrical maintenance","Plumbing repairs","Supply of PPE","Road maintenance","Building renovation","IT services"]

base=datetime.now()
for i in range(150):
  d,c=depts[i%len(depts)]
  ttl=titles[i%len(titles)]
  cl=(base+timedelta(days=5+i%25)).strftime("%Y-%m-%d")
  new_title=f"{ttl} {base.strftime('%Y%m%d')}-{i} - {d}"
  t.append({"title":new_title,"dept":d,"number":f"REF-{base.strftime('%Y%m%d')}-{i}","closing":cl,"category":c})

# 3. REMOVE DUPLICATES
seen=set()
unique=[]
for x in t:
  k=x.get('title')
  if k not in seen:
    seen.add(k)
    unique.append(x)
t=unique
print(f"TOTAL NOW: {len(t)}")

# 4. SAVE JSON + HTML COMBINED
open('tenders.json','w',encoding='utf-8').write(json.dumps(t,indent=2))

json_data=json.dumps(t)
html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Search {len(t)} Tenders</title></head><body style="font-family:Arial;padding:15px;background:#f4f4f4"><h2>🔍 Search {len(t)} Tenders</h2><input id="s" placeholder="Type cleaning, construction..." style="width:100%;padding:14px;border:2px solid #003366;border-radius:8px"><div id="r" style="margin-top:15px"></div><script>let data={json_data};document.getElementById('s').onkeyup=function(){{let q=this.value.toLowerCase();let f=data.filter(x=>JSON.stringify(x).toLowerCase().includes(q));document.getElementById('r').innerHTML=q.length<2?'Type to search':f.length+' found<br>'+f.slice(0,50).map(x=>'<div style=background:white;padding:12px;margin:8px 0;border-left:4px solid #003366;border-radius:8px><b>'+x.title+'</b><br>'+x.dept+' | '+x.number+' | '+x.closing+'<br><a href=https://wa.me/27787417326?text=PRO%20'+encodeURIComponent(x.title)+' style=background:#ff6600;color:white;padding:8px 12px;border-radius:6px;text-decoration:none;display:inline-block;margin-top:6px>🔒 PRO R150 Unlock</a></div>').join('')}}</script></body></html>"""
open('tenders.html','w',encoding='utf-8').write(html)

# 5. UPLOAD TO NEOCITIES
U=os.getenv('NEO_USER');P=os.getenv('NEO_PASS')
for fn in ['tenders.json','tenders.html']:
  try:
    r=requests.post('https://neocities.org/api/upload',auth=(U,P),files={fn:open(fn,'rb')})
    print(fn, r.text[:150])
  except Exception as e:
    print(e)
print(f"✅ DONE - TOTAL {len(t)} TENDERS SAVED - GROWING DAILY!")

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
depts=[("KZN Health","construction"),("Victory","cleaning"),("PRASA","electrical"),("Eskom","supply"),("DWS","security"),("SANRAL","IT")]
titles=["Replace Motor/Hoist","Cleaning gutters","Supply valves","Electrical maintenance","Security services","IT Support","Construction works"]
base=datetime.now()
for i in range(150):
    d,c=depts[i%len(depts)]
    ttl=titles[i%len(titles)]
    cl=(base+timedelta(days=5+i%25)).strftime("%Y-%m-%d")
    # Avoid duplicate
    if any(x['title']==ttl and x['dept']==d for x in t):
        continue
    t.append({"id":len(t)+1,"title":ttl,"dept":d,"category":c,"closing":cl,"date":base.strftime("%Y-%m-%d")})

print(f"TOTAL AFTER GROW: {len(t)}")

# 3. SAVE
with open('tenders.json','w',encoding='utf-8') as f:
    json.dump(t,f,indent=2)

html=f"<html><head><title>BS Tenders {len(t)}</title></head><body><h1>BS Tenders - {len(t)} Live - {base.strftime('%Y-%m-%d')}</h1>"
for x in t[-150:]:
    html+=f"<div><b>{x['title']}</b> - {x['dept']} - {x['closing']}</div>"
html+="</body></html>"
with open('tenders.html','w',encoding='utf-8') as f:
    f.write(html)

# 4. UPLOAD TO NEOCITIES
try:
    u=os.environ.get('NEO_USER')
    p=os.environ.get('NEO_PASS')
    if u and p:
        for fn in ['tenders.json','tenders.html']:
            with open(fn,'rb') as f:
                r=requests.post('https://neocities.org/api/upload',auth=(u,p),files={fn:f})
            print(fn, r.status_code)
except Exception as e:
    print(e)

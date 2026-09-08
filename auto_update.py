import requests, json, random
from datetime import datetime, timedelta
import os
USER = os.getenv('NEO_USER')
PASS = os.getenv('NEO_PASS')
r = requests.post('https://neocities.org/api/auth', data={'username': USER, 'password': PASS})
API_KEY = r.json()['api_key']
cats = ["Cleaning","Construction","Security","Catering","Supply & Delivery","ICT","Electrical","Plumbing"]
depts = ["Dept of Health","Dept of Education","City of Johannesburg","Ekurhuleni Municipality"]
locs = ["Gauteng","KZN","Western Cape","Limpopo"]
tenders = []
base = datetime.now() + timedelta(days=7)
for i in range(200):
    cat = random.choice(cats)
    dept = random.choice(depts)
    loc = random.choice(locs)
    closing = (base + timedelta(days=random.randint(1,60))).strftime("%Y-%m-%d")
    tenders.append({"id": i+1, "title": f"{cat} Services {1000+i} - {dept}", "dept": dept, "number": f"RFQ {100+i}/2026", "closing": closing, "type": cat, "category": cat, "location": loc, "source": "etenders.gov.za VERIFY", "note": "SAMPLE - Join PRO R150"})
with open('tenders.json','w') as f:
    json.dump(tenders, f, indent=2)
headers = {'Authorization': f'Bearer {API_KEY}'}
with open('tenders.json','rb') as f:
    files = {'tenders.json': f}
    up = requests.post('https://neocities.org/api/upload', headers=headers, files=files)
    print(up.json())

import os,requests
from datetime import datetime
U=os.getenv('NEO_USER')
P=os.getenv('NEO_PASS')
d=datetime.now().strftime('%d %B %Y %H:%M')
html=f"""<html><head><title>BS Daily Tenders</title>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<style>body{{font-family:Arial;background:#f5f5f5;margin:0}}.h{{background:#0a2a5e;color:white;padding:15px;text-align:center}}
.b{{background:white;margin:20px;padding:20px;border-radius:10px}}.t{{border-left:4px solid #ff6a00;padding:12px;margin:12px 0;background:#fff8f0}}
a{{background:#0a2a5e;color:white;padding:10px 18px;text-decoration:none;border-radius:6px;display:inline-block}}</style>
</head><body><div class='h'><h2>🔥 BS DAILY TENDERS</h2><p>{d}</p></div>
<div class='b'><h3>Latest Tenders</h3>
<div class='t'><b>Health:</b> Medical Supplies - Closing 15 Sep</div>
<div class='t'><b>Public Works GP:</b> Road Maintenance - Closing 18 Sep</div>
<div class='t'><b>Education:</b> School Furniture - Closing 20 Sep</div>
<div class='t'><b>COJ:</b> Cleaning Services - Closing 22 Sep</div>
<div class='t'><b>Transport:</b> Safety Equipment - Closing 25 Sep</div>
<p style='color:gray;font-size:12px'>Auto-updated daily 08:00 by BS Bot</p>
<a href='/'>← Back to Home</a> <a href='https://etenders.gov.za'>eTenders →</a></div></body></html>"""
open('tenders.html','w',encoding='utf-8').write(html)
r=requests.post('https://neocities.org/api/upload',auth=(U,P),files={'tenders.html':open('tenders.html','rb')})
print(r.text)
print("DONE - Home safe!")

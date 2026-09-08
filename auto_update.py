import os,requests
from datetime import datetime
U=os.getenv('NEO_USER')
P=os.getenv('NEO_PASS')
html=f"<html><head><title>BS Company Guide</title></head><body><h1>✅ BOT FIXED! BS Company Guide Live</h1><p>Updated: {datetime.now()}</p><p>Site: bscompanyguide.neocities.org</p><h2>Latest Tenders</h2><p>1. Dept Health - Medical Supplies</p><p>2. Municipality - Roads</p></body></html>"
open('index.html','w').write(html)
r=requests.post('https://neocities.org/api/upload',auth=(U,P),files={'index.html':open('index.html','rb')})
print(r.text)

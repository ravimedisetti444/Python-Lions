import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)
#print(info)


lst=info["comments"]
print('User count:', len(lst))
line2=list()

for item in lst:
    line2.append(int(item.get('count',0)))
    
print(sum(line2))


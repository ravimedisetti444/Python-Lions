# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = input('Enter Count- ')
position = input('Enter Position - ')
lst = list()

for i in range(int(count)):
    cn=0
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        cn=cn+1
        if(cn==int(position)):
            url=tag.get('href', None)
            lst.append(tag.contents[0])
    
print(lst)
    

#formato xml
#link para ejemplo   http://py4e-data.dr-chuck.net/comments_703286.xml
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

stuff = ET.fromstring(html)
lst= stuff.findall('comments/comment')
print(len(lst))

sum=0
for item in lst:
     sum= sum + float(item.find('count').text)
print(sum)

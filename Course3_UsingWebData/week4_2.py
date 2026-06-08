#formato html
#link para ejemplo http://py4e-data.dr-chuck.net/known_by_Heather.html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the anchor tags
tags = soup('a')

for x in range(1,8):
    counter=0
    for tag in tags:
        counter=counter + 1
        if counter == 18:
            #ver ejemplo 4.1, aca solo imprimo URL Y Contents
            print('URL:', tag.get('href', None))
            print('Contents:', tag.contents[0])
            url=tag.get('href', None)
            html = urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            # Retrieve all of the anchor tags
            tags= soup('a')

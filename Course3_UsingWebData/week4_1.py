#formato html
# link para ejemplo http://py4e-data.dr-chuck.net/comments_703284.html
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
# el tag que hay dentro de las comillas simples, es el que busca en todas las lineas de toda la pagina html
#en cualquier pagina, click izq,ver codifo de fuente de la pagina,
#ej: http://py4e-data.dr-chuck.net/comments_703284.html
#ejemplo de tags 1:  empiezan <a> y terminan </a>
#ejemplo de tags 2:  empiezan <span> y terminan </span>
tags = soup('span')
#aca se guarda lo que hay en los tags de SPAN, que hay en todas las lineas de la pagina, ordenados lineaxlinea
sum=0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Attrs:', tag.attrs)
    print('Contents:', tag.contents[0])
    sum= sum + int(tag.contents[0])
print(sum)

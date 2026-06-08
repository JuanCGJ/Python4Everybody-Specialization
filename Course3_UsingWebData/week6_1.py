#formato json
import json
import urllib.request, urllib.parse, urllib.error

url='http://py4e-data.dr-chuck.net/comments_703287.json'
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print(len(data), ' Characters')

js = json.loads(data)
# print(len(js)) #tamaño de documento js=2... 2 listas= Note y comments
NC=len(js['comments']) # tamaño de diccionarios comments=50
# print(NC)
#print(json.dumps(js, indent=4)) #dumps imprime la informacion en orden, bonita, indent= tamaño de letra
sum=0
for n in range(NC):
     count=js['comments'][n]['count'] #valor count de cada comment
     sum=sum+count
print(sum)

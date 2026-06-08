#programa base para ejercicio 6_2 location: University of West Florida
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


while True:
    address = input('Enter location: ')
    if len(address) < 1:
        address= 'University of West Florida';

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    print(js['results'][0]['place_id'])

    # diccionarios dentro de listas...listas de diccionarios
    # print(len(js['results']))  #tamaño 1
    # print(len(js['results'][0])) #tamaño 6
    # print(len(js['results'][0]['address_components'])) #tamaño 8
    # print(len(js['results'][0]['formatted_address'])) #tamaño 47
    # print(len(js['results'][0]['geometry']) #tamaño 3
    # print(len(js['results'][0]['place_id'])) #tamaño 27
    # print(len(js['results'][0]['plus_code'])) #tamaño 2
    # print(len(js['results'][0]['types'])) #tamaño 3

    #ejemplos para sacar el valor mas profundo dentro de una ruta # X
    # 1. print(js['results'][0]['geometry']['location']['lng'])
    # 2. print(js['results'][0]['types'][1])

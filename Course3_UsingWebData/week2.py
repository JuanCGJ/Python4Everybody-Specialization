import re
handle = open('regex_sum.txt')
lista=list()
suma=0

for line in handle:
    line.rstrip()
    y= re.findall('[0-9]+', line)
    for s in y:
        x=float(s)
        suma=suma+x
print(suma)

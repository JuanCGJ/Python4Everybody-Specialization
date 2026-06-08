name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
diction=dict()
hour=list()

for line in handle:
    if not line.startswith('From '):
        continue
    line=line.split()
    h=line[5]
    hour.append(h)

for c in hour:
    num=c[0:2]
    diction[num]=diction.get(num,0)+1

final=list()
for k,v in diction.items():
    fin=(k,v)
    final.append(fin)
    orden=sorted(final)

for k,v in orden:
        print(k,v)
        

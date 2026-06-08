name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails=dict()

for line in handle :
    if not line.startswith('From:'):
        continue
    wds=line.split()
    for l in wds:
        if not l == 'From:':
            mails[l]= mails.get(l,0) + 1

largo=-1
correo=None

for k,v in mails.items():
    if v > largo:
        largo=v
        correo=k

print(correo,largo)

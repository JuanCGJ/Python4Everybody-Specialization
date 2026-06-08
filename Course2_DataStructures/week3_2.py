# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=float(0)
add=float(0)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    x=line.find('0')
    num=line[20:]
    fnum=float(num)
    count=count+1
    fcount=float(count)
    add=add+fnum
    fadd=float(add)
print('Average spam confidence:', fadd/fcount)

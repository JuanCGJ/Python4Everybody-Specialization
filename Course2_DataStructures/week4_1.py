# Use the file name romeo.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst =list()

for line in fh:
    line=line.rstrip()
    line=line.split()
    for w in line:
        if w in lst:
            continue
        lst.append(w)
lst.sort()
print(lst)

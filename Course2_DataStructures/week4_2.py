# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh :
    line.rstrip()
    if not line.startswith('From:'):
        continue
    x=line.split()
    print(x[1])
    count=count+1

print("There were", count, "lines in the file with From as the first word")

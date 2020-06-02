fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst=list()
for line in fh:
    line=line.rstrip()
    line=line.split()
    if "From" in line:
        lst.append(line[5])
        count=count+1

line3=list()
counts=dict()
for line1 in lst:
    line1=line1.split(":")
    line3.append(line1[0])
    
line3=sorted(line3,reverse=True)
for hr in line3:
    counts[hr]=counts.get(hr,0)+1
for k,v in counts.items():
    print(k,v)

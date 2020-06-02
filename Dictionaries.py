fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts=dict()
email=''
cnt=0
lst=list()

for line in fh:
    line=line.rstrip()
    line=line.split()
    if "From" in line:
        lst.append(line[1])
for line1 in lst:
    counts[line1]=counts.get(line1,0)+1
bigcount=None
bigword=None

for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst=list()

for line in fh:
    line=line.rstrip()
    line=line.split()
    if "From" in line:
        print(line[1])
        lst.append(line)
        count=count+1
print("There were", count, "lines in the file with From as the first word")

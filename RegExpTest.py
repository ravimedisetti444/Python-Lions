import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_42.txt"

fh = open(fname)
count = 0

lst=list()
result=list()

for line in fh:
    line=line.rstrip()
    line=line.split()
    lst=re.findall('[0-9]+',str(line))
    for lst1 in lst:
        result.append(int(lst1))
print(sum(result))

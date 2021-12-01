from pdb import set_trace as br
import csv

mylist = []
i=0
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for line in c:
        mylist.append(int(line[0]))
sumlist=[]
for [i,j] in enumerate(mylist):
    if i<(2000-2):
        sum=mylist[i]+mylist[i+1]+mylist[i+2]
        sumlist.append(sum)
count=0
for [i,j] in enumerate(sumlist):
    if i>0:
        if sumlist[i]>sumlist[i-1]:
            count+=1
print(count)
from pdb import set_trace as br
import csv

mylist = []
mylist2 = [0]
i=0
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for line in c:
        mylist.append(int(line[0]))
        if i!=0:
            if mylist[i]>mylist[i-1]:
                mylist2.append(1)
            if mylist[i]<mylist[i-1]:
                mylist2.append(-1)
            else:
                mylist2.append(0)
        i+=1
j = 0
for i in mylist2:
    if (i == 1):
        j+=1
print(j)

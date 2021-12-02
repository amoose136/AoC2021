from pdb import set_trace as br
import csv

mylist = []
mylist2 = [0]
i=0
x=0
y=0
aim=0
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for instruction in c:
        direction=instruction[0]
        val=instruction[1]
        if (direction=='down'):
            aim+=int(val)
        elif(direction=='up'):
            aim-=int(val)
            if (y<0):
                y=0
        else:
            x+=int(val)
            y+=aim*int(val)
print(x)
print(y)
print(x*y)
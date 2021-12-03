from pdb import set_trace as br
import csv

mylist = []
mbits = [0 for i in range(0,12)]
count=0
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for bits in c:
        for [i,bit] in enumerate(bits[0]):
            mbits[i]+=int(bit)
            count+=1
for [i,bit] in enumerate(mbits):
    mbits[i]=int(float(bit)*12/count+.5)
number=""
for bit in mbits:
    number=number+str(bit)
gamma=int(number,2)
epsilon=int('111111111111',2)-int(number,2)
print(gamma)
print(format(epsilon,'b'))
print(gamma*epsilon)

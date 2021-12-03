from pdb import set_trace as br
import csv

mylist = []
mbits = [0 for i in range(0,12)]
count=0
stringbits=[]
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for bits in c:
        stringbits.append(bits[0])
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
O2mask=number[0]
O2stringbits=stringbits
CO2stringbits=stringbits
pos=0
while(len(O2stringbits)>1):
    count=len(O2stringbits)
    val=0
    for b in O2stringbits:
        val+=int(b[pos])
    O2mask=str(int(float(val)/count+.5))
    O2stringbits=[b for b in O2stringbits if b[pos] == O2mask]
    pos+=1
pos=0
while(len(CO2stringbits)>1):
    count=len(CO2stringbits)
    val=0
    for b in CO2stringbits:
        val+=int(b[pos])
    CO2mask=str(1-int(float(val)/count+.5))
    CO2stringbits=[b for b in CO2stringbits if b[pos] == CO2mask]
    pos+=1
print(O2stringbits[0])
print(int(CO2stringbits[0],2)*int(O2stringbits[0],2))
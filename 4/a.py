from pdb import set_trace as br
import csv
import numpy as np

rawinput=[]
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for a in c:
        rawinput.append(a)
nums=[int(a) for a in rawinput[0][0].split(',')]
rawgamefields=rawinput
rawgamefields.pop(0) # remove first item
rawgamefields=[i for i in rawgamefields if i!=[]]
gamefields=[]
for i in range(0,100):
    temparr=[]
    for j in range(0,5):
        temparr.append(rawgamefields[i*5+j])
    temparr2=[]
    for [i,k] in enumerate(temparr):
        line=[]
        for num in k:
            line.append(int(num))
        temparr2.append(line)
    gamefields.append(temparr2)

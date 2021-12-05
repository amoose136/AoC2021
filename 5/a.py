from pdb import set_trace as br
import csv
import numpy as np

rawinput=[]
lines=[]
mp=np.zeros((1000,1000),dtype=np.int8)
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for a in c:
        rawinput.append(a)
        x1=int(a[0].split(',')[0])
        y1=int(a[0].split(',')[1])
        x2=int(a[2].split(',')[0])
        y2=int(a[2].split(',')[1])
        if x1==x2:
            mp[x1,min(y1,y2):max(y1,y2)+1]+=1
        elif y2==y1: #same y value
            mp[min(x1,x2):max(x1,x2)+1,y2]+=1
print(mp[mp>1].shape)
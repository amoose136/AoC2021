from pdb import set_trace as br
import csv
import numpy as np

rawinput=[]
lines=[]
mp=np.zeros((1000,1000),dtype=np.int32)
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for a in c:
        rawinput.append(a)
        x1=int(a[0].split(',')[1])
        y1=int(a[0].split(',')[0])
        x2=int(a[2].split(',')[1])
        y2=int(a[2].split(',')[0])
        if x1==x2:
            # x=0
            mp[x1,min(y1,y2):max(y1,y2)+1]+=1
        elif y2==y1: #same y value
            # x=0
            mp[min(x1,x2):max(x1,x2)+1,y2]+=1
        else:
            length=max(x1-x2,x2-x1)
            littlex=min(x1,x2)
            for l in range(0,length+1):
                if x1<x2:
                    if y1<y2:
                        mp[x1+l,y1+l]+=1
                    else:
                        mp[x1+l,y1-l]+=1
                else:
                    if y1<y2:
                        mp[x1-l,y1+l]+=1
                    else:
                        mp[x1-l,y1-l]+=1
print(mp[mp>1].shape)
print(mp)
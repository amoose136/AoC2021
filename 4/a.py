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
completed_in=np.zeros(100,dtype=int)
scores=np.zeros(100,dtype=int)
completed=np.zeros(100,dtype=int)
index=0
remaining=len([i for i in completed if i == 0])
while(remaining==100):
    for [i,field] in enumerate(gamefields):
        if completed[i]==0:
            for [j,row] in enumerate(field):
                field[j]=[10000 if val==nums[index] else val for val in row]
            gamefields[i]=field
    for [i,val] in enumerate(completed):
        if val!=1:
            completed_in[i]+=1
    for [i,field] in enumerate(gamefields):
        if completed[i]==0:
            # row like:
            for row in range(0,5):
                sum=0
                for col in range(0,5):
                    sum+=field[row][col]
                if sum>=50000:
                    completed[i]=1
                    break
            # col like
            for row in range(0,5):
                sum=0
                for col in range(0,5):
                    sum+=field[col][row]
                if sum>=50000:
                    completed[i]=1
                    break
    index+=1
    remaining=len([i for i in completed if i == 0])
winningboard=np.array(gamefields[completed.tolist().index(1)])
winningboard=winningboard.reshape(-1).tolist()
winningboard=[i if i!=10000 else 0 for i in winningboard]
score=np.sum(winningboard)*nums[index-1]
print(score)
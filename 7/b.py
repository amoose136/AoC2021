from pdb import set_trace as br
import numpy as np

with open('input.txt') as f:
    positions=np.array([int(p) for p in f.readlines()[0].split(',')])
totalCost=np.zeros(np.max(positions))
for [i,cost] in enumerate(totalCost):
    for j in np.abs(i-positions):
        totalCost[i]+=np.sum(range(0,j+1))
    if i>=1 and totalCost[i]>totalCost[i-1]:
        print(totalCost[i-1])
        break
# Current algorithm is slow as hell but it *does* solve the problem in under a minute....#NoRefactors
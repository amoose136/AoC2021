from pdb import set_trace as br
import numpy as np

with open('input.txt') as f:
    positions=np.array([int(p) for p in f.readlines()[0].split(',')])
median=round(np.median(positions))
cost=np.sum(np.abs(median-positions))
print(cost)
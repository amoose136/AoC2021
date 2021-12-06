from pdb import set_trace as br
import csv
import numpy as np

ages=np.array([])
with open('input.txt') as f:
    c = csv.reader(f, delimiter=' ',skipinitialspace=True)
    for a in c:
        ages=a[0].split(',')
for [i,a] in enumerate(ages):
    ages[i] = int(a)
for t in range(0,80):
    for [i,a] in enumerate(ages):
        if a>0:
            ages[i]-=1
            continue
        elif a==0:
            ages[i]=6
            ages.append(9)
            continue
    # print(t)
print(len(ages))
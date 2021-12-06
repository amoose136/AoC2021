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
ages=np.array(ages)
populations=[]
for i in range(0,9):
    populations.append(len(ages[ages==i]))
print(populations)
for t in range(0,256):
    resets=populations[0]
    populations[0]=populations[1]
    populations[1]=populations[2]
    populations[2]=populations[3]
    populations[3]=populations[4]
    populations[4]=populations[5]
    populations[5]=populations[6]
    populations[6]=populations[7]+resets
    populations[7]=populations[8]
    populations[8]=resets
    # Okay I'm not proud that the above didn't compress a section of it into a loop but that's how it was when I left it.  #noRefactoringAllowed
print(sum(populations))
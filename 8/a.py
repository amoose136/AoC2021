from pdb import set_trace as br
import numpy as np

with open('input.txt') as f:
    input = f.readlines()
inputs=[]
outputs=[]
for val in input:
    inputs.append(val.strip().split('|')[0].strip().split(' '))
    outputs.append(val.strip().split('|')[1].strip().split(' '))
inputs = np.array(inputs)
outputs = np.array(outputs)
# number    |   Number of segments
# 0         |   6
# 1         |   2 <-
# 2         |   5
# 3         |   5
# 4         |   4 <-
# 5         |   5
# 6         |   6
# 7         |   3 <-
# 8         |   7 <-
# 9         |   6
count=0
lengthChecker=np.vectorize(len)
outputlengths=lengthChecker(outputs)
for line in outputlengths:
    for i in line:
        if i in [2,4,3,7]:
            count+=1
print(count)
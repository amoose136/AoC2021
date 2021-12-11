from io import IncrementalNewlineDecoder
from os import lseek
from pdb import set_trace as br
import numpy as np

with open('input.txt') as f:
    input = f.readlines()
    input = [i.strip() for i in input]
ninput = []
for i in input:
    t=[]
    for c in i:
        t.append(int(c))
    ninput.append(t)
input=np.array(ninput)
flashCount=0


# input[y][x]
def mymod(a,b):
    return a%b
mod=np.vectorize(mymod)
width=len(input[:,0])
height=len(input[0,:])

def flash(y,x):
    if (y>0):
        if(x<width-1):
            input[y-1,x+1]+=1
        input[y-1,x]+=1
        if(x>0):
            input[y-1,x-1]+=1
    if(x>0):
        input[y,x-1]+=1
    if(x<width-1):
        input[y,x+1]+=1
    
    if (y<height-1):
        if(x<width-1):
            input[y+1,x+1]+=1
        input[y+1,x]+=1
        if(x>0):
            input[y+1,x-1]+=1
    input[y,x]-=2000
    global flashCount
    flashCount+=1

def increment(a):
    return a+1
inc=np.vectorize(increment)
for i in range(0,100):
    input=inc(input)
    while(len(input[input>9])>0):
        for [y,line] in enumerate(input):
            for [x,val] in enumerate(line):
                if val>9:
                    flash(y,x)
    for [y,line] in enumerate(input):
        for [x,val] in enumerate(line):
            if val<0:
                input[y,x]=0
print(flashCount)
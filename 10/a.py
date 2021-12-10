from io import IncrementalNewlineDecoder
from pdb import set_trace as br
import numpy as np

with open('reducedinput.txt') as f:
    input = f.readlines()
    input = [i.strip() for i in input]
def scope(c):
    if c in '()':
        return 0
    elif c in '[]':
        return 1
    elif c in '\{\}':
        return 2
    elif c in '<>':
        return 3
    else:
        return -1 #error
s_paren=0
s_square=0
s_curly=0
s_angle=0
incomplete=[]
error=False
for [x,line] in enumerate(input):
    s = scope(line[0])
    old_s=[]
    if line[0] in ']}>)':
        print('bad opening')
    error=False
    for [i,character] in enumerate(line):
        if character in ')]}>':
            if scope(character)!=s:
                if character==')':
                    s_paren+=1
                elif character==']':
                    s_square+=1
                elif character=='}':
                    s_curly +=1
                elif character=='>':
                    s_angle +=1
                error=True
                break
            else:
                s=old_s[-1]
                old_s.pop()
        else:
            old_s.append(s)
            s=scope(character)
    if error==False:
        incomplete.append(input[x])
paren=0
square=0
curly=0
angle=0
print( ') :' + str(s_paren))
print( '] :' + str(s_square))
print( '} :' + str(s_curly))
print( '> :' + str(s_angle))
print(s_paren*3+s_square*57+s_curly*1197+s_angle*25137)
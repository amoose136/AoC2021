from io import IncrementalNewlineDecoder
from pdb import set_trace as br
import numpy as np

with open('input.txt') as f:
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


scores=[]
score=0
for line in incomplete:
    cache=[0]
    for character in line:
        if character == cache[-1]:
            cache.pop()
        elif character == '(':
            cache.append(')')
        elif character == '[':
            cache.append(']')
        elif character == '{':
            cache.append('}')
        elif character == '<':
            cache.append('>')
    cache.pop(0)
    cache.reverse()
    string=''
    score=0
    for s in cache:
        score*=5
        if s==')':
            score+=1
        elif s==']':
            score+=2
        elif s=='}':
            score+=3
        elif s=='>':
            score+=4
    print(line," =", score)
    scores.append(score)
print("median score =", int(np.median(scores)))
from pdb import set_trace as br
import numpy as np

with open('reducedinput.txt') as f:
    input = f.readlines()
inputs=[]
outputs=[]
for val in input:
    inputs.append(val.strip().split('|')[0].strip().split(' '))
    outputs.append(val.strip().split('|')[1].strip().split(' '))
inputs = np.array(inputs)
outputs = np.array(outputs)
# number    |   Number of segments
# 0         |   6          len(0 + 1)=6 -> len(0+4)=7
# 1         |   2 <- given for free
# 2         |   5       2-4-7 = eg 2-7=deg len(deg)+len(eg)=5
# 3         |   5       3-4-7 = g  3-7=dg  len(dg)+len(g)=3
# 4         |   4 <- given for free, contains 1
# 5         |   5       5-4-7 = g  5-7=bdg len(bdg)+len(g)=4
# 6         |   6           len(6 + 1)==7
# 7         |   3 <- given for free, contains 1
# 8         |   7 <- given for free, coptains 1
# 9         |   6           len(9 + 1)=6  -> len(9+4)=6
count=0
lengthChecker=np.vectorize(len)
inputlengths=lengthChecker(inputs)
def encodeToBinary(string):
    num=0
    for [i,digit] in enumerate('abcdefg'):
        if digit in string:
            num+=2**i
    return num
encodeArrToBinary=np.vectorize(encodeToBinary)
binaryInputs=encodeArrToBinary(inputs)
uniqueLengths=[2,4,3,7]
for [i,line] in enumerate(inputs):
    binaryIndex=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    binaryValue=[0,0,0,0,0,0,0,0,0,0]
    #freebee numbers 1,4,7,8
    for [j,k] in enumerate([1,4,7,8]):
        binaryIndex[k]=np.where(inputlengths[i]==uniqueLengths[j])[0][0]
        binaryValue[k]=binaryInputs[i][binaryIndex[k]]
    # br()
    minus47=(binaryInputs[i] & binaryValue[4]) & binaryValue[7]
    minus7=binaryInputs[i] & binaryValue[7]
    plus1=binaryInputs[i] | binaryValue[1]
    plus4=binaryInputs[i] | binaryValue[4]
    for j in range(0,10):
        mlength=inputlengths[i][j]
        if mlength in uniqueLengths:
            continue
        elif mlength==5:
            length=len([k for k in format(minus7[j],'b') if k=='1'])+len([k for k in format(minus47[j],'b') if k=='1'])
            if length==3:
                print('found 3')
                binaryIndex[3]=j
                binaryValue[3]=binaryInputs[i][j]
                continue
            # elif length==5:
            #     print('found 2')
            #     binaryIndex[2]=j
            #     binaryValue[2]=binaryInputs[i][j]
            #     continue
            # elif length==4:
            #     print('found 5')
            #     binaryIndex[5]=j
            #     binaryValue[5]=binaryInputs[i][j] 
            #     continue
        # if mlength==6:
        #     length=len([k for k in format(plus1[j],'b') if k == '1'])
        #     if length==7:
        #         binaryIndex[6]=j
        #         binaryValue[6]=binaryInputs[i][j]
        #         continue
        #     elif length==6:
        #         length=len([k for k in format(plus4[j],'b') if k=='1'])
        #         if length==6:
        #             binaryIndex[9]=j
        #             binaryValue[9]=binaryInputs[i][j]
        #             continue
        #         elif length==7:
        #             binaryIndex[0]=j
        #             binaryValue[0]=binaryInputs[i][j]
        #             continue
    if i==0:
        print(binaryIndex)
        for j in range(0,10):
            for k in range(0,10):
                if binaryIndex[k]==j:
                    print(inputs[0][j]+' = ' +str(k))
            
# Written by Yizheng Ying for COMP9021


# Insert your code here

import sys
import re
file_name = str(input('Which data file do you want to use? '))
try:
    fp = open(file_name)
except IOError:
    print('Error!It is not exist!')
    sys.exit
pf = []
lane = []
line = fp.readline()
while line:
    length = len(line)
    result=re.split(r'[\nR(,)]',line)
    
    for i in result:
        if i=='':
            result.remove(i)
    print(result)
    lane=[int(result[0]),int(result[1])]
    pf.append(lane)
    line = fp.readline()
fp.close

def find_way(pf):
    save=[]
    for tail in range(len(pf)):
        for head in range(len(pf)):
            if pf[tail][1]==pf[head][0]:
                if [pf[tail][0],pf[head][1]] not in save:
                    save.append([pf[tail][0],pf[head][1]])
    return save

temp=find_way(pf)
for xtemp in range(len(temp)):
    for ypf in range(len(pf)):
        if temp[xtemp] not in pf:
            if temp[xtemp][1]==pf[ypf][0] and [temp[xtemp][0],pf[ypf][1]] not in temp:
                temp.append([temp[xtemp][0],pf[ypf][1]])

for n in temp:
    if n in pf:
        pf.remove(n)
print('The nonredundant facts are:')
for m in pf:
    print('R('+str(m[0])+','+str(m[1])+')')



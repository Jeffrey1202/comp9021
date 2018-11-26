
# Written by Yizheng Ying for COkg_to_sendP9021


# Insert your code here

import sys

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
    pt = [int(i) for i in line.split()]
    pf.append(pt)
    line = fp.readline()

fp.close
L2 = []
total=0
max_kg_to_get=0
min_kg=pf[0][1]
for i in range(len(pf)):
    L2.append(int(pf[i][1]))
    total += pf[i][1]
    if min_kg > pf[i][1]:
        min_kg = pf[i][1]
average=total//len(pf)
aim=int((average+min_kg)/2)


def find_largest_kg(aim):
    kg_to_send=[]
    for i in range(len(pf)):
        kg_to_send.append(pf[i][1])
    for j in range(len(kg_to_send)-1):
        distance=pf[j + 1][0] - pf[j][0]
        available=kg_to_send[j] - aim
        if (available>0):
            if (available> distance):
                kg_to_send[j + 1] += available - distance
            if (available <= distance):
                continue
        elif(available<0):
            kg_to_send[j+1]+=  available - distance
    return kg_to_send[-1]-aim


while True:
    if find_largest_kg(aim)<0:
        average=aim
        aim=(average+min_kg)/2
        if max_kg_to_get-aim <0.01 and max_kg_to_get-aim >-0.01:
            break
    elif find_largest_kg(aim)>0:
        min_kg=aim
        aim=(average+min_kg)/2
    else:
        break
    max_kg_to_get=aim
    
result=str(int(max_kg_to_get))
print('The maximum quantity of fish that each town can have is '+result+'.')





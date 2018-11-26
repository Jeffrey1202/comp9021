# Written by Yizheng Ying for COMP9021


# Insert your code here

import sys

file_name = str(input('Which data file do you want to use? '))
try:
    fp = open(file_name)
except IOError:
    print('Error!It is not exist!')
    sys.exit
pf = []
line = []
line = fp.readline()
while line:
    length = len(line)
    pt = [int(i) for i in line.split()]
    pf.append(pt)
    line = fp.readline()

fp.close

x_list=[]
y_list=[]
for x in pf:
    x_list.append([x[1],x[0],x[2],'button'])
    x_list.append([x[3],x[0],x[2],'top'])
    y_list.append([x[0],x[1],x[3],'button'])
    y_list.append([x[2],x[1],x[3],'top'])


def perimeter(line):
    tested_list=[]
    sum1=0
    temp=0
    for list_to_test in line:
        part_list=[list_to_test[0],list_to_test[1]]
        if list_to_test[2]=='button':
            tested_list.append(part_list)
        else:
            tested_list.remove(part_list)
        if len(tested_list)!=0:
            temp_list=[]
            for line1 in tested_list:
                temp_list.append(line1[0])
                temp_list.append(line1[1])
            temp_list=sorted(temp_list)
            overlapping=temp_list[-1]-temp_list[0]
            for j in range(len(temp_list)-1):
                middle=(temp_list[j+1]+temp_list[j])/2
                [flag,judgement]=judge(middle,tested_list,temp_list[j+1],temp_list[j],overlapping)
                if flag:
                    overlapping=judgement
        else:
            overlapping=0
            
        if overlapping>=temp:
            sum1+=overlapping-temp
        elif overlapping<temp:
            sum1+=(temp-overlapping)
        temp=overlapping
    return sum1

def judge(middle,line,a,b,c):
    for x in line:
        if middle <x[1] and middle> x[0]:
            return [False,c]
    return [True,c-(a-b)]

x_list=sorted(x_list)
y_list=sorted(y_list)
x_end=[]
y_end=[]
for i in x_list:
    x_end.append(i[1:4])
for j in y_list:
    y_end.append(j[1:4])

result=perimeter(x_end)+perimeter(y_end)
print('The perimeter is: '+str(result))


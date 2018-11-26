# Written by Yizheng Ying for COMP9021


# Insert your code here
import sys
import copy

file_name = str(input('Which data file do you want to use? '))
try:
    fp = open(file_name)
except IOError:
    print('Error!It is not exist!')
    sys.exit
count = 0
pf = []
lane = []
line = fp.readline()
while line:
    # print(line)
    count += 1
    length = len(line)
    pt = [int(i) for i in line.split()]
    pf.append(pt)
    line = fp.readline()
# print(pf)
fp.close

record_line = [[]]
record = []
sum1 = []
for i in range(len(pf) - 1, -1, -1):
    i_back = len(pf) - i - 1
    sum1.append([])
    record_line.append([])
    record.append([])
    for j in range(0, len(pf[i])):
        if i + 1 == len(pf):
            sum1[0].append(pf[i][j])
            record[0].append(1)
            record_line[0].append([pf[i][j]])
        
        if i + 1 < len(pf) and sum1[i_back-1][j]==sum1[i_back-1][j+1]:
            sum1[i_back].append(pf[i][j]+sum1[i_back-1][j])
            record[i_back].append(record[i_back-1][j]+record[i_back-1][j+1])
            record_line[i_back].append(copy.deepcopy(record_line[i_back-1][j]))
            record_line[i_back][j].append(pf[i][j])
        if i + 1 < len(pf) and sum1[i_back - 1][j] > sum1[i_back - 1][j + 1]:
            sum1[i_back].append(pf[i][j] + sum1[i_back - 1][j])
            record[i_back].append(record[i_back - 1][j])
            record_line[i_back].append(copy.deepcopy(record_line[i_back - 1][j]))
            record_line[i_back][j].append(pf[i][j])
        
        if i + 1 < len(pf) and sum1[i_back - 1][j] < sum1[i_back - 1][j + 1]:
            sum1[i_back].append(pf[i][j] + sum1[i_back - 1][j+1])
            record[i_back].append(record[i_back - 1][j+1])
            record_line[i_back].append(copy.deepcopy(record_line[i_back - 1][j+1]))
            record_line[i_back][j].append(pf[i][j])
          
# print(record)

record1=[]
for i in range(len(record_line[len(pf)-1][0])-1,-1,-1):
    record1.append(record_line[len(pf)-1][0][i])
print('The largest sum is:', sum1[len(pf)-1][0])
print('The number of paths yielding this sum is:', record[len(pf)-1][0])
print('The leftmost path yielding this sum is:', record1)


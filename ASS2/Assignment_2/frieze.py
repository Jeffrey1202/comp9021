import sys
import re
import os
#from array import array
#import datetime
 
class FriezeError(Exception):
    def __init__(self,message):
        self.message=message
        
class Frieze:
    
    def __init__(self,filename):
        matrix = None
        #self.start=datetime.datetime.now()
        self.filename=filename
        
        if filename:
            matrix=self.__read_file__(filename)
        self.matrix=matrix
        self.dictionary={0:[],1:[1],2:[2],3:[2,1],4:[4],5:[4,1],6:[4,2],
                         7:[4,2,1],8:[8],9:[8,1],10:[8,2],11:[8,2,1],
                         12:[8,4],13:[8,4,1],14:[8,4,2],15:[8,4,2,1]}
        self.ns_lines=self.n_s_lines()
        self.nwse_lines=self.nw_se_lines()
        self.we_lines=self.w_e_lines()
        self.swne_lines=self.sw_ne_lines()
        
        
        
    def __read_file__(self,filename):
        matrix=[]
       
        try:
            with open(filename,'r') as file:
                linelist=file.readlines()
                length=0
                for item in linelist:
                    item=item.strip('\n')
                    split_item=item.split(' ')
                    #temp=''.join(split_item)
                    digit_list=list(split_item)
                    while '' in digit_list:
                        digit_list.remove('')
                    #print(digit_list)

                    if len(digit_list)==0:
                        continue
                    if length<len(digit_list):
                        
                        length=len(digit_list)
                    temp_list=[]
                    for list_number in digit_list:
                        if list_number!='':
                            number=int(list_number)
                            if number<0 or number>15:
                                raise FriezeError('Incorrect input.')
                            if length<5 or length>51:
                                raise FriezeError('Incorrect input.')
                            temp_list.append(number)
##                        except ValueError:
##                            print('Incorrect input.')
##                            sys.exit()
##                        except LengthError:
##                            print('Incorrect input.')
##                            sys.exit()
##                        else:
##                            raise FriezeError('Incorrect input.')
                    
                    matrix.append(temp_list)
               
                for row in matrix:
                    #print(matrix)
                    if len(row)<length:
                        raise FriezeError('Incorrect input.')
                        sys.exit()
        except FileNotFoundError:
            print('Incorrect file name or file not found, giving up.')
            sys.exit()
        #print(matrix)
        if len(matrix)<3 or len(matrix)>17:
            raise FriezeError('Incorrect input.')
        for i in range(len(matrix[0])-1):
                    if matrix[0][i]!=4 and matrix[0][i]!=12:
                        raise FriezeError('Input does not represent a frieze.')
        if matrix[0][-1]!=0:
            raise FriezeError('Input does not represent a frieze.')
        for i in range(1,len(matrix)):
            if matrix[i][-1]!=0 and matrix[i][-1]!=1:
                print(matrix[i][-1])
                raise FriezeError('Input does not represent a frieze.')
            for j in range(len(matrix[0])):
                if matrix[i-1][j]>=8 and matrix[i][j]>=2 and matrix[i][j]<=3:
                    raise FriezeError('Input does not represent a frieze.')
        for i in range(len(matrix[-1])):
            if matrix[-1][i]>=8:
                raise FriezeError('Input does not represent a frieze.')
        period=0
        for i in range(1,len(matrix)-1):
            if period<self.caculate_period(matrix[i]) and self.caculate_period(matrix[i])!=0:
                period=self.caculate_period(matrix[i])
        if period==0:
            raise FriezeError('Input does not represent a frieze.')
        return matrix

    def analyse(self):
        matrix=self.matrix
        temp=self.find_matrix()
        period=self.judge_period()
        period=int(period)
        flag1=self.judge_horizantal(temp)
        flag2=self.judge_vertical(temp)
        flag3=self.judge_glided_horizontal(temp)
        flag4=self.judge_rotation(temp)
        #print(flag1,flag2,flag3,flag4)
        if not flag1 and not flag2 and not flag3 and not flag4:
            print('Pattern is a frieze of period',period,'that is invariant under translation only.')
        elif flag1 and not flag2 and not flag3 and not flag4:
            print('Pattern is a frieze of period',period,'that is invariant under translation')
            print('        and horizontal reflection only.')
        elif not flag1 and flag2 and not flag3 and not flag4:
            print('Pattern is a frieze of period',period,'that is invariant under translation')
            print('        and vertical reflection only.')
        elif not flag1 and not flag2 and flag3 and not flag4:
            print('Pattern is a frieze of period',period,'that is invariant under translation')
            print('        and glided horizontal reflection only.')
        elif not flag1 and not flag2 and not flag3 and flag4:
            print('Pattern is a frieze of period',period,'that is invariant under translation')
            print('        and rotation only.')
        elif flag1 and flag2:
            print('Pattern is a frieze of period',period,'that is invariant under translation,')
            print('        horizontal and vertical reflections, and rotation only.')
        elif flag3 and flag2:
            print('Pattern is a frieze of period',period,'that is invariant under translation,')
            print('        glided horizontal and vertical reflections, and rotation only.')
##        elif flag1 and flag4:
##            print('Pattern is a frieze of period',period,'that is invariant under translation,')
##            print('        horizontal and vertical reflections, and rotation only.')
##        elif flag3 and flag4:
##            print('Pattern is a frieze of period',period,'that is invariant under translation,')
##            print('        glided horizontal and vertical reflections, and rotation only.')
#        end=datetime.datetime.now()
 #       print(end-self.start)

        
    def find_matrix(self):
        matrix=self.matrix
        matrix_1=self.matrix_1
        matrix_2=self.matrix_2
        matrix_4=self.matrix_4
        matrix_8=self.matrix_8
        
        temp=[[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        #print(temp)
        for i in range(len(matrix_2)):
            while '' in matrix_2[i]:
                matrix_2[i].remove('')
            while '' in matrix_8[i]:
                matrix_8[i].remove('')
        mlen=len(matrix_1)
        for i in range(mlen):
            for j in range(len(matrix_1[0])):
                if matrix_1[i][j]!=0:
                    temp[i][j]+=1
                if matrix_2[i][j]!=0:
                    temp[i][j]+=1
                if matrix_4[i][j]!=0:
                    temp[i][j]+=1
                if matrix_8[i][j]!=0:
                    temp[i][j]+=1
        return temp
    
    def judge_horizantal(self,temp):
        matrix=self.matrix
        #temp=self.find_matrix()
        mlen=len(matrix)
##        for i in range(mlen):
##            print(temp[i])
        flag=True
        for j in range(len(matrix[0])):
            for i in range(mlen//2):
                if temp[i][j]==temp[mlen-i-1][j]:
                    continue
                else:
                    flag=False
        if flag:
            return True
        else:
            return False

    def judge_vertical(self,temp):
        period=0
        flag=False
        length=len(temp)
        for i in range(length):
            #print(temp[i])
            if period<self.caculate_period(temp[i]) and self.caculate_period(temp[i])!=0:
                period=self.caculate_period(temp[i])
        period=int(period)
        for x in range(len(temp[0])-period):
            #print(x,x+period,x+period*2-1,x+period-1)
            count=0
            for y in range(length):
                #print(temp[y][x:(x+period)],temp[y][(x+period*2-1):(x+period-1):-1])
                if temp[y][x:(x+period)]==temp[y][(x+period*2-1):(x+period-1):-1]:   
                    count+=1
            if count==length:
                flag=True
        if not flag:
            for i in range(len(temp[0])//2+1):
                count1=0
                for j in range(len(temp)):
                    if temp[j][:i]==temp[j][len(temp[0])-1:i:-1]:
                        count1+=1
                if count1==length:
                    flag=True
        return flag
            
    def judge_glided_horizontal(self,temp):
        period=0
        #temp=self.find_matrix()
        flag=True
        length=len(temp)
        for i in range(length):
            #print(temp[i])
            if period<self.caculate_period(temp[i]) and self.caculate_period(temp[i])!=0:
                period=self.caculate_period(temp[i])
        halfperiod=int(period/2)
        for j in range(len(temp[0])-halfperiod-1):
            for i in range(length//2):
                #print(temp[i][j+halfperiod],temp[length-i-1][j])
                if temp[i][j+halfperiod]==temp[length-i-1][j]:
                    continue
                else:
                    flag=False
        return flag
        
    def judge_rotation(self,temp):
        period=0
        #temp=self.find_matrix()
        flag=True
        length=len(temp)
        height=len(temp[0])
        rotated=list(zip(*temp[::-1]))
        rotated1=list(zip(*rotated[::-1]))
        #print(height)
        for i in range(length):
            if tuple(temp[i])==rotated1[i]:
                continue
            else:
                flag=False
##                print(True)
##            print(temp[i])
##            print(rotated1[i])
##            print()
##            if period<self.caculate_period(temp[i]) and self.caculate_period(temp[i])!=0:
##                period=self.caculate_period(temp[i])
##        period=int(period)
##        #print(height//2)
##        for j in range(height-2*period-1):
##            for i in range(length):
##                #print(temp[i][j:(j+period)],temp[length-i-1][(j+period*2):(j+period):-1])
##                if temp[i][j:(j+period)]==temp[length-i-1][(j+period*2):(j+period):-1]:
##                    continue
##                else:
##                    flag=False
        return flag

    def judge_period(self):
        period=0
        matrix=self.matrix
        for i in range(1,len(matrix)-1):
            if period<self.caculate_period(matrix[i]) and self.caculate_period(matrix[i])!=0:
                period=self.caculate_period(matrix[i])
        if period>=2:
            return period
        else:
            return 0
    
    def caculate_period(self,temp):
        period=0
        times=0
        result=[]
        flag=True
        for i in range(1,len(temp)//2+1):
            list1=temp[:i]
            count=0
            for j in range(1,(len(temp)-1)//i):
                list2=temp[i*j:i*(j+1)]
                if list1==list2:
                    count+=1
                if (count+1)*len(list2)==len(temp)-1:
                    times=count+1
                    result.append(times)
                    #print(list2)
                    #print(result[0])
        if len(result)>0:
            period=(len(temp)-1)/result[0]
            return period
        else:
            return 0

        
    def display(self):
        output_list=[]
        output_list.append('\\documentclass[10pt]{article}\n')
        output_list.append('\\usepackage{tikz}\n')
        output_list.append('\\usepackage[margin=0cm]{geometry}\n')
        output_list.append('\\pagestyle{empty}\n\n')
        output_list.append('\\begin{document}\n\n')
        output_list.append('\\vspace*{\\fill}\n')
        output_list.append('\\begin{center}\n')
        output_list.append('\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n')

        ns_lines=self.ns_lines
        nwse_lines=self.nwse_lines
        we_lines=self.we_lines
        swne_lines=self.swne_lines
# % North to South lines
        output_list.append('% North to South lines\n')
        for i in range(len(ns_lines)):
            output_list.append('    \\draw '+str(ns_lines[i][0]).replace(' ','')+' -- '+str(ns_lines[i][1]).replace(' ','')+';\n')
# % North-West to South-East lines
        output_list.append('% North-West to South-East lines\n')
        for i in range(len(nwse_lines)):
            output_list.append('    \\draw '+str(nwse_lines[i][0]).replace(' ','')+' -- '+str(nwse_lines[i][1]).replace(' ','')+';\n')           
# % West to East lines
        output_list.append('% West to East lines\n')
        for i in range(len(we_lines)):
            output_list.append('    \\draw '+str(we_lines[i][0]).replace(' ','')+' -- '+str(we_lines[i][1]).replace(' ','')+';\n')
# % South-West to North-East lines
        output_list.append('% South-West to North-East lines\n')
        for i in range(len(swne_lines)):
            output_list.append('    \\draw '+str(swne_lines[i][0]).replace(' ','')+' -- '+str(swne_lines[i][1]).replace(' ','')+';\n')

        output_list.append('\\end{tikzpicture}\n')
        output_list.append('\\end{center}\n')
        output_list.append('\\vspace*{\\fill}\n\n')
        output_list.append('\\end{document}\n')

        filename=self.filename
        filename=os.path.splitext(filename)[0]
        output_file=filename+'.tex'
        try:
            with open(output_file, 'w') as myfile:
                myfile.write(''.join(output_list))
        except IOError:
            print('Can not output frieze to tex file.')

    def find_lines(self,aim):
        matrix=self.matrix
        dictionary=self.dictionary
        temp=[[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num=matrix[i][j]
                if aim in dictionary[num]:
                    temp[i][j]=aim
        return temp

    def n_s_lines(self):
        temp1=[]
        result=[]
        aim=[]
        temp=self.find_lines(1)
        temp2=self.find_lines(1)
        for i in range(len(temp[0])):
            for j in range(1,len(temp)):
                if temp[j][i]==1:
                    temp[j][i]=(i,j)
                    temp[j-1][i]=(i,j-1)
        self.matrix_1=temp
        for i in range(len(temp[0])):
            for j in range(len(temp)):
##                if temp2[j][i]==0 and temp[j][i]!=0 and len(temp1)==0:
##                    temp1.append(temp[j][i])
##                elif temp2[j][i]!=0:
##                    temp1.append(temp[j][i])
##                elif temp2[j][i]==0 and len(temp1)>0 and temp[j][i]!=0:
##                    result.append(temp1)
##                    temp1=[]
                if j==0:
                    if temp[j][i]!=0:
                        temp1.append(temp[j][i])
                else:
                    if temp2[j-1][i]!=0 and temp2[j][i]==0 and len(temp1)>0 and temp[j-1][i]!=0:
                        result.append(temp1)
                        temp1=[]
                        if temp[j][i]!=0:
                            temp1.append(temp[j][i])
                    elif temp[j][i]!=0:
                        temp1.append(temp[j][i])
            if len(temp1)>0:
                result.append(temp1)
                temp1=[]
                      
        for i in range(len(result)):
            #print(result[i])
            aim.append([result[i][0],result[i][-1]])
        #for i in range(len(aim)):
            #print(aim[i])
        return aim


    def sw_ne_lines(self):
        temp=self.find_lines(2)
        row=len(temp)
        col=len(temp[0])
        temp1=[['' for i in range(len(temp[0])+len(temp)-1)] for i in range(len(temp))]
        temp2=[['' for i in range(len(temp[0])+len(temp)-1)] for i in range(len(temp))]
        temp3=[]
        result=[]
        aim=[]
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                temp1[i][i+j]=temp[i][j]
                temp2[i][i+j]=temp[i][j]
        #for i in range(len(temp1)):
           # print(temp1[i])
        for i in range(len(temp1[0])):
            for j in range(1,len(temp1)):
                if temp1[j][i]==2:
                    temp1[j][i]=(i-j,j)
                    temp1[j-1][i]=(i-j+1,j-1)
        self.matrix_2=temp1
       # for i in range(len(temp1)):
            #print(temp1[i])
        for i in range(len(temp1[0])):
            for j in range(len(temp1)):
                if j==0:
                    if temp1[j][i]!=0 and temp1[j][i]!='':
                        temp3.append(temp1[j][i])
                else:
                    if temp2[j-1][i]!=0 and temp2[j-1][i]!='' and temp2[j][i]==0 and len(temp3)>0 and temp1[j-1][i]!=0 and temp1[j-1][i]!='':
                        result.append(temp3)
                        temp3=[]
                        if temp1[j][i]!=0 and temp1[j][i]!='':
                            temp3.append(temp1[j][i])
                    elif temp1[j][i]!=0 and temp1[j][i]!='':
                        temp3.append(temp1[j][i])
                    
                    
            if len(temp3)>0 and temp2 not in result:
                result.append(temp3)
                temp3=[]
        #for i in range(len(result)):
            #print(result[i])
        for i in range(len(result)):
            aim.append([result[i][-1],result[i][0]])
        aim=sorted(aim,key=lambda x:(x[0][1],x[0][0]))
        #for i in range(len(aim)):
            #print(aim[i])
        return aim
                
    def w_e_lines(self):
        temp1=[]
        result=[]
        aim=[]
        temp=self.find_lines(4)
        temp2=self.find_lines(4)
        for i in range(len(temp)):
            for j in range(len(temp[0])-1,-1,-1):
                if temp[i][j]==4:
                    temp[i][j]=(j,i)
                    temp[i][j+1]=(j+1,i)
        #for i in range(len(temp)):
            #print(temp2[i])
        self.matrix_4=temp
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if temp2[i][j]!=0:
                    temp1.append(temp[i][j])
                elif temp2[i][j]==0 and len(temp1)>0 and temp[i][j]!=0:
                    temp1.append(temp[i][j])
                    result.append(temp1)
                    temp1=[]
            if len(temp1)>0:
                result.append(temp1)
                temp1=[]
        for i in range(len(result)):
            aim.append([result[i][0],result[i][-1]])
            #print(result[i])
        
        #for i in range(len(aim)):
           # print(aim[i])
        return aim

    def nw_se_lines(self):
        temp=self.find_lines(8)
        temp1=[['' for i in range(len(temp[0])+len(temp)-1)] for i in range(len(temp))]
        temp2=[['' for i in range(len(temp[0])+len(temp)-1)] for i in range(len(temp))]
        temp3=[]
        result=[]
        aim=[]
        for i in range(len(temp)):
            for j in range(len(temp[0])-1,-1,-1):
                temp1[i][len(temp)-1-i+j]=temp[i][j]
                temp2[i][len(temp)-1-i+j]=temp[i][j]
        
        for i in range(len(temp1[0])-1,-1,-1):
            for j in range(len(temp1)-1,-1,-1):
                if temp1[j][i]==8:
                    temp1[j][i]=(j-len(temp1)+1+i,j)
                    temp1[j+1][i]=(j-len(temp1)+i+2,j+1)
        self.matrix_8=temp1
        #for i in range(len(temp1)):
           # print(temp1[i])
        #for i in range(len(temp1)):
            #print(temp2[i])
        for i in range(len(temp1[0])):
            for j in range(len(temp1)):
                if j==0:
                    if temp1[j][i]!=0 and temp1[j][i]!='':
                        temp3.append(temp1[j][i])
                else:                     
                    if temp2[j][i]!=0 and temp2[j][i]!='':
                        temp3.append(temp1[j][i])
                    elif temp2[j][i]==0 and len(temp3)>0 and temp1[j][i]!=0 and temp1[j][i]!='':
                        temp3.append(temp1[j][i])
                        result.append(temp3)
                        temp3=[]
##                        if temp1[j][i]!=0 and temp1[j][i]!='':
##                            temp3.append(temp1[j][i])
                    
                  
            if len(temp3)>0 and temp2 not in result:
                result.append(temp3)
                temp3=[]
        #for i in range(len(result)):
            #print(result[i])
        for i in range(len(result)):
            aim.append([result[i][0],result[i][-1]])
        aim=sorted(aim,key=lambda x:(x[0][1],x[0][0]))
        #for i in range(len(aim)):
            #print(aim[i])
        return aim

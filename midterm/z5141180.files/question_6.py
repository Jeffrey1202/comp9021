
def display(square):
    print('\n'.join(' '.join(f'{x:2d}' for x in row) for row in square))

def check_out_square_and_fix_if_corrupted(square):
    '''
    Call "good square" an n x n matrix with n >= 2 consisting of all numbers
    between 1 and n ** 2.
    Call "corrupted square" a good square exactly one of whose entries has been
    replaced by 0.

    Note: marks can be scored by just checking whether the square is good or corrupted,
    without fixing it in case it is corrupted -- but hard coding won't help.
    
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6  4  8
    It is a good square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 10, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6 10  8
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 0],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  0
     6  4  8
    It is a corrupted square, the good square being:
     1  5  7
     2  9  3
     6  4  8
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [2, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     2  9  0 16
     6  4  8 12
    13 14 15  2
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [3, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     3  9  0 16
     6  4  8 12
    13 14 15  2
    It is a corrupted square, the good square being:
     1  5  7 11
     3  9 10 16
     6  4  8 12
    13 14 15  2
    '''
    n = len(square)
    if n < 2 or any(len(line) != n for line in square):
        return False
    print('Here is the square: ')
    display(square)
    good_square = False
    corrupted_square = False
    # Insert your code here
    length=len(square)
    S=[]
    S1=[]
    flag=0
    a=0
    square1=[]
    
    count=1
    for i in range(length*length):
        S.append(i+1)
    for x in square:
        for y in x:
            S1.append(y)
    for x in square:
        for y in x:
            if len(list(set(S1)))!=length*length:
                corrupted_square=False
                flag=1
            else:
                if y not in S and y!=0:
                    corrupted_square=False
                    flag=1
                elif y==0:
                    corrupted_square=True
                    flag=1
    if flag==0:
        good_square=True
    if corrupted_square:
        for i in range(len(S)):
            if S[i] not in S1:
                a=S[i]
        for j in range(len(S1)):
            if S1[j]==0:
                S1[j]=a
        R1=[S1[0]]
        for x in range(1,length*length):
            if count%length==0:
                square1.append(R1)
                R1=[S1[x]]
            else:
                R1.append(S1[x])
            count+=1
        square1.append(R1)
        square=square1
                

    
    if good_square:
        print('It is a good square.')
    else:
        if not corrupted_square:
            print('It is neither a good nor a corrupted square.')
        else:
            print('It is a corrupted square, the good square being:')
            display(square)

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

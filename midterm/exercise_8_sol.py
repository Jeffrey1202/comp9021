
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    
    S=[]
    length=len(square)
    sum3=0
    sum4=0
    for i in square:
        sum1=0
        for j in i:
            sum1+=j
        if sum1 not in S:
            S.append(sum1)
    for i in range(length):
        sum2=0
        for j in range(length):
            sum2+=square[j][i]
        if sum2 not in S:
            S.append(sum2)
    for x in range(length):
        sum3+=square[x][x]
        sum4+=square[x][length-1-x]
    if sum3 not in S:
        S.append(sum3)
    if sum4 not in S:
        S.append(sum4)
    if len(S)==2*length+2:
        print(True)
    else:
        print(False)
            
        



    


   
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

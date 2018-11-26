

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    S=[]
    R=[]
    R2=[]
    for e in word:
        S.append(ord(e))
    R1=[S[0]]
    for i in range(1,len(S)):
        if S[i]==S[i-1]+1:
            R1.append(S[i])
        else:
            R.append(R1)
            R1=[S[i]]
    R.append(R1)
    for e in R:
        if len(e)>desired_length:
            desired_length=len(e)
            R2=e
    for i in R2:
        desired_substring+=chr(i)
        
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

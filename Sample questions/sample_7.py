'''
Tries and find a word in a text file that represents a grid of words, all of the same length.
There is only one word per line in the file.
The letters that make up a word can possibly be separated by an arbitrary number of spaces,
and there can also be spaces at the beginning or at the end of a word,
and there can be lines consisting of nothing but spaces anywhere in the file.
Assume that the file stores data as expected.

A word can be read horizontally from left to right,
or vertically from top to bottom,
or diagonally from top left to bottom right
(this is more limited than the lab exercise).
The locations are represented as a pair (line number, column number),
starting the numbering with 1 (not 0).
'''


def find_word(filename, word):
    '''
    >>> find_word('word_search_1.txt', 'PLATINUM')
    PLATINUM was found horizontally (left to right) at position (10, 4)
    >>> find_word('word_search_1.txt', 'MANGANESE')
    MANGANESE was found horizontally (left to right) at position (11, 4)
    >>> find_word('word_search_1.txt', 'LITHIUM')
    LITHIUM was found vertically (top to bottom) at position (2, 14)
    >>> find_word('word_search_1.txt', 'SILVER')
    SILVER was found vertically (top to bottom) at position (2, 13)
    >>> find_word('word_search_1.txt', 'SODIUM')
    SODIUM was not found
    >>> find_word('word_search_1.txt', 'TITANIUM')
    TITANIUM was not found
    >>> find_word('word_search_2.txt', 'PAPAYA')
    PAPAYA was found diagonally (top left to bottom right) at position (1, 9)
    >>> find_word('word_search_2.txt', 'RASPBERRY')
    RASPBERRY was found vertically (top to bottom) at position (5, 14)
    >>> find_word('word_search_2.txt', 'BLUEBERRY')
    BLUEBERRY was found horizontally (left to right) at position (13, 5)
    >>> find_word('word_search_2.txt', 'LEMON')
    LEMON was not found
    '''
    with open(filename) as file:
        grid = None
        gridtemp=[]
        # Insert your code here
        grid = [''.join(c for c in line if not c.isspace())for line in file if not line.isspace()]
        #with open(filename) as file:
           # for line in file:
           #    temp=[]
            #    if not line.isspace():
            #        for c in line:
              #          if c!=' ' and c!='\n':
              #              temp.append(c)
             #       gridtemp.append(temp)
          #  grid=gridtemp
        # A one liner that sets grid to the appropriate value is enough.
        location = find_word_horizontally(grid, word)
        found = False
        if location:
            found = True
            print(word, 'was found horizontally (left to right) at position', location)
        location = find_word_vertically(grid, word)
        if location:
            found = True
            print(word, 'was found vertically (top to bottom) at position', location)
        location = find_word_diagonally(grid, word)
        if location:
            found = True
            print(word, 'was found diagonally (top left to bottom right) at position', location)
        if not found:
            print(word, 'was not found')
    
    
def find_word_horizontally(grid, word):
    length=len(word)
    for i in range(0,len(grid)):
        for j in range(len(grid[i])-length):
            w=''.join(grid[i][k] for k in range(j,j+length))
            if w==word:
                return (i+1,j+1)
            
                       
    # Replace pass above with your code


def find_word_vertically(grid, word):
    length=len(word)
    for i in range(0,len(grid)-length):
        for j in range(len(grid[i])):
            w=''.join(grid[k][j] for k in range(i,i+length))
            if w==word:
                return (i+1,j+1)

    # Replace pass above with your code


def find_word_diagonally(grid, word):
    length=len(word)
    for i in range(0,len(grid)-length+1):
        for j in range(len(grid[i])-length+1):
            w=''.join(grid[i+k][j+k] for k in range(0,length))
            if w==word:
                return (i+1,j+1)
    # Replace pass above with your code


if __name__ == '__main__':
    import doctest
    doctest.testmod()   

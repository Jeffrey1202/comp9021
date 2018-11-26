# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint


dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

# Possibly define other functions

try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner  = 0

global b
b=[[0]*dim for _ in range(dim)]
def homogenous(i,j):
    if grid[0][0]==grid[i][j]:
        b[i][j]=1
        if i-1>=0 and b[i-1][j]!=1:
            homogenous(i-1,j)
        if i+1<dim and b[i+1][j]!=1:
            homogenous(i+1,j)
        if j-1>=0 and b[i][j-1]!=1:
            homogenous(i,j-1)
        if j+1<dim and b[i][j+1]!=1:
            homogenous(i,j+1)
    return

homo=0
homogenous(0,0)
for i in range(dim):
    for j in range(dim):
        homo+=b[i][j]

size_of_largest_homogenous_region_from_top_left_corner=homo
# Replace this comment with your code
print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = 0
# Replace this comment with your code
c=[[0]*dim for _ in range(dim)]


def checker(i,j,flag):
    if flag!=grid[i][j]:
        c[i][j]=1
        if i-1>=0 and c[i-1][j]!=1:
            checker(i-1,j,grid[i][j])
        if i+1<10 and c[i+1][j]!=1:
            checker(i+1,j,grid[i][j])
        if j-1>=0 and c[i][j-1]!=1:
            checker(i,j-1,grid[i][j])
        if j+1<10 and c[i][j+1]!=1:
            checker(i,j+1,grid[i][j])
    return

ck=0
max_ck=0
for i in range(dim):
    for j in range(dim):
        c=[[0]*dim for _ in range(dim)]
        ck=0
        if grid[i][j]==0:
            end=1
        else:
            end=0
        checker(i,j,end)
        for row in range(dim):
            for col in range(dim):
                ck+=c[row][col]

        if ck>max_ck:
            max_ck=ck

max_size_of_region_with_checkers_structure=max_ck
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )




            


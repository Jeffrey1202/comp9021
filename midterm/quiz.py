import sys
from random import seed, randint


dim = 10
grid = [[None] * dim for _ in range(dim)]


def display_grid():
     for i in range(dim):
         print('    ', end = '')
         for j in range(dim):
             if grid[i][j]:
                 print(' 1', end = '')
             else:
                 print(' 0', end = '')
         print()
     print()

def display_my_grid(L):
     for i in range(dim):
         print('    ', end = '')
         for j in range(dim):
             print(L[i][j], end = ' ')
         print()
     print()

def copy_grid_to_temp_grid():
     for i in range(dim):
         for j in range(dim):
             temp_grid[i][j] = grid[i][j]

def copy_temp_grid_to_grid():
     for i in range(dim):
         for j in range(dim):
             grid[i][j] = temp_grid[i][j]

def count_no_check_cell_value():
     return_value = 0
     for i in range(dim):
         for j in range(dim):
             if grid[i][j] == no_check_cell_value:
                 return_value += 1
     return return_value


no_check_cell_value = 2
my_temp_sum = 0
def explore_from(i, j):
     if grid[i][j] == no_check_cell_value or i > (dim-1) or j > (dim-1) or i < 0 or j < 0:
         return
     current_cell_value = grid[i][j]
     # print(i, j, current_cell_value)
     grid[i][j] = no_check_cell_value
     if i+1 < dim and current_cell_value != grid[i+1][j]:
         # print(i+1, j, grid[i+1][j])
         explore_from(i+1, j)
     if j+1 < dim and current_cell_value != grid[i][j+1]:
         explore_from(i, j+1)
     if current_cell_value != grid[i-1][j] and (i-1) > 0:
         explore_from(i-1, j)
     if current_cell_value != grid[i][j-1] and (j-1) > 0:
         explore_from(i, j-1)


 # REPLACE PASS ABOVE WITH YOUR CODE


provided_input = input('Enter 2 integers, '
                        'the second one being nonnegative: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
     print('Incorrect input, giving up.')
     sys.exit()
try:
     seed_arg, density, = (int(i) for i in provided_input)
     if density < 0:
         raise ValueError
except:
     print('Incorrect input, giving up.')
     sys.exit()

seed(seed_arg)

for i in range(dim):
     for j in range(dim):
         grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

max_size_of_region_with_checkers_structure = 0
 # REPLACE THIS COMMENT WITH YOUR CODE
sum_t = 0
temp_grid = [[None] * dim for _ in range(dim)]
for i in range(dim):
     for j in range(dim):
         copy_grid_to_temp_grid()
         # print('Staring position {} {}'.format(i, j))
         explore_from(i, j)
         sum_t = count_no_check_cell_value()
         if sum_t > max_size_of_region_with_checkers_structure:
             max_size_of_region_with_checkers_structure = sum_t
             print(i, j)
             display_my_grid(grid)
         # print('Grid changed value')
         # display_my_grid(grid)
         copy_temp_grid_to_grid()
         # print('Grid reset value')
         # display_my_grid(grid)

print('The size of the largest area with a checkers structure '
 'is {}'.format(max_size_of_region_with_checkers_structure))

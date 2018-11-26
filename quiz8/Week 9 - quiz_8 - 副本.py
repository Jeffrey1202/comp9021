# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by yizheng ying and Eric Martin for COMP9021


import sys
from random import seed, randrange
import datetime

from queue_adt import *

start=datetime.datetime.now()
def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def leftmost_longest_path_from_top_left_corner():
    # Replace pass above with your code
    queue = Queue()
    direction = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    gridlen = len(grid)
    total_path=[]
    for i in range(gridlen):
        for j in range(gridlen):
            total_path.append((i,j))
    temp = []
    changelist = []
    aim = []
    len_of_leftmost=0
    if grid[0][0] == 0:
        return None
    elif grid[0][0] == 1:
        temp.append((0, 0))
        queue.enqueue(temp)
        while queue.__len__() != 0:
            start = queue.dequeue()
            if len_of_leftmost<len(start):
                aim=start
            #print(len(start))
            # print(start)
            if start == [(0, 0)]:
                changelist = [direction['N'], direction['E'], direction['S']]
            elif len(start) > 1:
                temp1 = start[-1]
                temp2 = start[-2]
                x = temp1[0] - temp2[0]
                y = temp1[1] - temp2[1]
                if x == 0 and y == 1:
                    changelist = [direction['N'], direction['E'], direction['S']]
                elif x == 1 and y == 0:
                    changelist = [direction['E'], direction['S'], direction['W']]
                elif x == -1 and y == 0:
                    changelist = [direction['W'], direction['N'], direction['E']]
                else:
                    changelist = [direction['S'], direction['W'], direction['N']]
            path = []
            startx = start[-1][0]
            starty = start[-1][1]
            for point in changelist:
                pointx = point[0] + startx
                pointy = point[1] + starty
                if (pointx,pointy) in total_path:
                    if grid[pointx][pointy] != 0 and (pointx, pointy) not in start:
                        tem=list(start)
                        tem.append((pointx, pointy))
                        queue.enqueue(tem)
            len_of_leftmost = len(start)
    return aim


provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path})')

end=datetime.datetime.now()
print(end-start)

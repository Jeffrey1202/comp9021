# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree import *

# Possibly define some functions
leaves = []

def traverse(tree):
    # print(tree.value)
    if tree is not None:
        if tree.left_node is not None and tree.right_node is not None:
            if tree.left_node.value is None and tree.right_node.value is None:
                leaves.append(tree.value)
    else:
        return
    traverse(tree.left_node)
    traverse(tree.right_node)

def find_all_possible_leaves(tree):
    traverse(tree)
    print(traverse(tree))

def max_diff_in_consecutive_leaves(tree):
    pass
    # Replace pass above with your code
    find_all_possible_leaves(tree)
    #print(leaves)
    max_diff = 0
    for index in range(0, len(leaves)-1):
        t = abs(leaves[index] - leaves[index+1])
        if t > max_diff:
            max_diff = t

    return max_diff

provided_input = input('Enter two integers, the second one being positive: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0:
        raise ValueError
except:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))

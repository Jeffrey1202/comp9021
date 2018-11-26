# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

# Possibly define some functions
children=[]
def node_without_child(tree):
    if tree is None:
        return
    else:
        if tree.left_node is not None and tree.left_node.value is None\
           and tree.right_node is not None and tree.right_node.value is None:
            children.append(tree.value)
    if tree.left_node.value is not None:
        node_without_child(tree.left_node)
    if tree.right_node.value is not None:
        node_without_child(tree.right_node)

            
def max_diff_in_consecutive_leaves(tree):
    # Replace pass above with your code
    difference=0
    node_without_child(tree)
    len_children=len(children)
    if len_children>=2:
        for i in range(1,len_children):
            if children[i-1]>children[i]:
                temp=children[i-1]-children[i]
            else:
                temp=children[i]-children[i-1]
            if temp>difference:
                difference=temp
    return difference
            


provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
           

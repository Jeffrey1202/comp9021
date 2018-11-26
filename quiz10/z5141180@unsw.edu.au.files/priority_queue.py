# Written by yizheng ying for COMP9021


from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()
    
    def insert(self, value):
        #pass
        # Replace pass above with your code
        pre_nodes=[]
        if self.value is None:
            self.value=value
            self.left_node=BinaryTree()
            self.right_node=BinaryTree()
        else:
            height1=self._height()
            node_num=self.size()+1
            pre_nodes.append(self)
            height=int(log(self.size()+1,2))
            #print('h',height,'h1',height1)
            temp=self
            
            height_nodes_num=2**height
            pre_num=height_nodes_num

            count=1
            while count<height:
                height_nodes_num=int(height_nodes_num/2)
                if height_nodes_num+pre_num<=node_num:
                    pre_num=pre_num+height_nodes_num
                    temp=temp.right_node
                elif height_nodes_num+pre_num>node_num:
                    temp=temp.left_node
                pre_nodes.append(temp)
                count+=1
            if node_num!=pre_num:
                temp.right_node=BinaryTree(value)
                parent=temp.right_node
            else:
                temp.left_node=BinaryTree(value)
                parent=temp.left_node

            while pre_nodes!=[]:
                #print(pre_nodes[0].value)
                children=parent
                parent=pre_nodes[-1]
                pre_nodes=pre_nodes[1:len(pre_nodes)-1]
                if children.value<parent.value:
                   children.value,parent.value=parent.value,children.value 


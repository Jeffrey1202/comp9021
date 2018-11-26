# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        
        index_smallest=0
        if len(self)<2:
            return
        head=self.head
        smallest=head.value
        length=self.__len__()
        while head.next_node:
            if smallest>head.next_node.value:
                smallest=head.next_node.value
                index_smallest=self.index_of_value(smallest)
            head=head.next_node
        head.next_code=self.head
        index_pre=index_smallest-1
        head=self.head
        #print(temp)
        while index_pre:
            head=head.next_node
            index_pre-=1
        pre_node=head
        current_node=pre_node.next_node
        self.head=pre_node.next_node
        x=(length-1)//2
        while x:
            next_node2=current_node.next_node
            current_node.next_node=pre_node
            current_node=current_node.next_node.next_node
            pre_node.next_node=current_node
            pre_node=next_node2
            x-=1
        current_node.next_node=pre_node
        pre_node.next_code=None
        
    
    

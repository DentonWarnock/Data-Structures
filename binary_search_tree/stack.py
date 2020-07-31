"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList, Node
# Stack - last in first out

# Stack using array
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) <= 0:
            return None
        else:
            self.size -= 1
            removed_item = self.storage.pop()
            return removed_item
        
        
# Stack using SLL
class Stack:
    def __init__(self):
        self.head = None
        self.tail =  None
        self.size = 0
        # self.storage = LinkedList()
        
    def __len__(self):
        return self.size
        
    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
            
    def pop(self):
        if self.head is None:
            return None
        else:
            self.size -= 1
            removed_value = self.head.value
            self.head = self.head.get_next()
            return removed_value
        
        
    

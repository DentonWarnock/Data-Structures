"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# Queue - first in first out
from singly_linked_list import LinkedList, Node

# Array
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.insert(0, value)
        return self.storage[0]

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            self.size -= 1
            removed_item = self.storage.pop()
            return removed_item
        

# SLL
class Queue:
    def __init__(self):        
        self.storage = LinkedList()
        self.size = 0
        
    
    def __len__(self):
        return self.size    
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.storage.head is None:
            self.size += 1
            self.storage.head = new_node
            self.storage.tail = new_node
        else:
            self.size += 1
            new_node.next_node = self.storage.head
            self.storage.head = new_node
        
    def dequeue(self):
        # empty list
        if self.storage.head is None:
            return None
        # 1 item in list
        elif self.storage.head == self.storage.tail:
            removed_value = self.storage.tail.get_value()
            self.storage.head = None
            self.storage.tail = None
            self.size -= 1
            return removed_value
        # 2 or more items in list
        else:
            self.size -= 1
            return self.storage.remove_tail()
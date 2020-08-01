class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
        
    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0: # if self.head is None and self.tail is None   
            self.tail = new_node
        self.length += 1
        
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node            
        else: 
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
        
    def remove_head(self):
        # empty SLL
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None    
            self.length -= 1
            return value        
        # list with +2 Nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        # empty SLL
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1    
            return value 
        # list with +2 Nodes
        else:
            current_node = self.head
            while current_node.get_next() is not self.tail:
                current_node = current_node.get_next()
            value = self.tail.get_value()
            self.tail = current_node
            self.tail.set_next(None)
            self.length -= 1
            return value
        
    
    def contains(self, value):
        if self.head is None:
            return False        
        #Loop through each node until we see the value, or we cannot go further
        current_node = self.head        
        while current_node is not None:
            #check if this is the node we are looking for
            if current_node.get_value() == value:
                return True            
            #otherwise, go to the next node
            current_node = current_node.get_next()
        return False
    
    def get_max(self):
        # empty list
        if self.head is None: 
            return None
        # non-empty list
        # iterate through all items
        current_node = self.head
        current_max = self.head.get_value()
        while current_node is not None:
            if current_node.get_value() > current_max:
                current_max = current_node.get_value()
            current_node = current_node.get_next()
            
        return current_max
    
linked_list = LinkedList()
    
linked_list.add_to_head(0)
linked_list.add_to_head(1)
print(f'does LL contain 0? {linked_list.contains(0)}')
print(f'does LL contain 1? {linked_list.contains(1)}')
print(f'does LL contain 2? {linked_list.contains(2)}')

linked_list.add_to_head(5)
print(f'the start of the list is: {linked_list.head.value}')
print(f'the max of the list is: {linked_list.get_max()}')

linked_list.remove_head()
linked_list.remove_tail()
print(f'the start of the list is: {linked_list.head.value}')
print(f'the max of the list is: {linked_list.get_max()}')

linked_list.add_to_tail(7)
print(f'the end of the list is: {linked_list.tail.value}')
print(f'the max of the list is: {linked_list.get_max()}')

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if tree is empty make value = root
        if self.value is None:
            self.value = BSTNode(value)       
        # compare to the new value we want to insert        
        # if new value <= self.value
        
        elif value < self.value:
            # IF self.left is already taken by a node
            if self.left is not None:
                # make that (left) node call insert
                self.left.insert(value)
            # set the left to the new node with the new value
            else:
                self.left = BSTNode(value)
            
        # if new value > self.value
        elif value >= self.value:
            # IF self.right is already taken by a node
            if self.right is not None:
                # make that (right) node call insert
                self.right.insert(value)
            # set the right child to the new node with new value (update current node to be current_node.right)
            else:
                self.right = BSTNode(value)        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # end goal - if target is equal to the root node
        if self.value == target:
            return True
        # compare the target to current value        
        found = False # setting default
        if target < self.value:
            # check the left subtree
            # if you cannot go left, return False
            if self.left is None:
                return False
            # if there is a left node, make that node call contains
            found = self.left.contains(target) # use recursion to return True or False
        # if current value > target
        if target >= self.value:
            #check if right subtree contains target
            # if you cannot go right return False
            if self.right is None:
                return False
            # if there is a right node, make that node call contains
            found = self.right.contains(target) # use recursion to return True or False
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will be on the bottom right of our tree
        # go right if you can, otherwise return current node's value
        if self.right is not None:
            return self.right.get_max()
        return self.value           
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  

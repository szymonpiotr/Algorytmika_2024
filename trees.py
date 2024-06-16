class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(10)
root.right.right.right = Node(11)

def is_element(root, element):
   if root.left == None and root.right == None:
      return element == root.data
   else:
      return (is_element(root.left, element) or is_element(root.right, element))

def how_many(root):
   if root.left == None and root.right == None:
      return 1 
   else:
      return how_many(root.left) + how_many(root.right) + 1 
   
def is_balanced(root):
   if root.left == None and root.right == None:
      return True
   else:
      return abs(how_many(root.left) - how_many(root.right)) <= 1

def subtree_balanced(root):
   if root.left == None and root.right == None:
      return True
   else:
      return is_balanced(root) and subtree_balanced(root.left) and subtree_balanced(root.right)

  

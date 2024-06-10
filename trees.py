class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
root.right.right.right = Node(7) 

def is_element(root, element):
   if root.left == None and root.right == None:
      return element == root.data
   else:
      return (is_element(root.left, element) or is_element(root.right, element))

  

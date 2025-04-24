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

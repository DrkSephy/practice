# Write a function to find the second largest element in 
# a binary search tree.

class BinaryTreeNode:

  def __init__(self, value):
      self.value = value
      self.left  = None
      self.right = None

  def insert_left(self, value):
      self.left = BinaryTreeNode(value)
      return self.left

  def insert_right(self, value):
      self.right = BinaryTreeNode(value)
      return self.right


# Find largest element in a tree
def find_largest(root):
  if root is None:
    raise Exception('Tree must have at least 1 node')
  if root.right is not None:
    return find_largest(root.right)
  return root.value

def find_second_largest(root):
  if root is None or root.left is None or root.right is None:
    raise Exception('Tree must have at least 2 nodes')

  # We are currently at the largest, and
  # largest has a left substree, find largest in that subtree
  if root.left and not root.right:
    return find_largest(root.left)

  # Else, we are currently at the parent of the largest, and largest
  # has no left subtree, therefore this node is second largest
  if root.right and not root.right.left and not root.right.right:
    return root.value

  # Otherwise, keep going right
  return find_second_largest(root.right)

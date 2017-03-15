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
# It'll take O(h), O(h) time (where h is the height of the tree) and O(h) O(h) space.
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


# O(h) time, O(1) space. Do it in one walk down the tree, not using a call stack from recursion
# 1. If we have a left subtree but not a right subtree, then the current node
#    is the largest. To find the second largest, get largest in left subtree
# 2. If we have a right child which doesn't have children, then the right child is
#    the largest node, the current node is the second largest
# 3. Else, we have a right subtree with more than one element, so we keep stepping right
def find_largest(root):
  current = root
  while current:
    if not current.right:
      return current.value
    current = current.right # Keep going right

def find_second_largest(root):
  if root is None or root.left is None and root.right is None:
    raise Exception('Tree must have at least 2 nodes')

  current = root

  while current:
    # Case: current is largest and has a left subtree
    # 2nd largest is largest in left subtree
    if current.left and not current.right:
      return find_largest(current.left)

    # Case: right child with no children, then the current node is second largest
    if current.right and current.right.right is None:
      return current.value

    # Case: More right-most children, keep stepping right
    current = current.right

# O(h) time, where hh is the height of the tree (again, that's O(\lg{n})O(lgn) 
# if the tree is balanced, O(n)O(n) otherwise). O(1)O(1) space.

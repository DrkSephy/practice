# Write a function to see if a binary tree is 
# "superbalanced" (a new tree property we just made up).

# A tree is "superbalanced" if the difference between the depths of 
# any two leaf nodes is no greater than one.

# We want to short-circuit as quickly as possible to save time.
# In order to quickly go through leaf nodes, we use DFS.

# Walk through the tree with DFS, keep track of a list of depths
# if we haven't seen it before.

# Each time we find a leaf node, our tree might be imbalanced:
#    1. There are more than 2 different leaf depths
#    2. There are exactly 2 different leaf depths and they are more than 1 apart.

# Complexity of solution: O(n) time and O(n) space


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

def is_balanced(root):
  # A tree with no nodes is superbalanced, since there are no leaves
  if root == None:
    return True

  # We short circuit as soon as find more than 2
  depths = []

  # Treat this list as a stack of tuples (node, depth). DFS implementation
  nodes = []
  nodes.append((root, 0))

  while(len(nodes)):

    # pop a node and get it's depth from our stack
    node, depth = nodes.pop()

    # Did we find a leaf?
    if (not node.left) and (not node.right):

      # We only care if it is a new depth
      if depth not in depths:
        depths.append(depth)

        # Two ways to have an unbalanced tree
        # 1. more than 2 different leaf depths
        # 2. 2 leaf depths are more than 1 apart
        if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
          return False

    # Case: not a leaf
    else:
      # Append right first so that left is popped first
      if node.right:
        nodes.append((node.right, depth + 1))
      if node.left:
        nodes.append((node.left, depth + 1))
  return True



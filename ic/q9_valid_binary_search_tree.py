# Write a function to check whether or not a 
# Binary tree (tree where each node has up to 2 children)
# is a valid binary search tree.

# Depth-first traversal of a tree uses memory proportional to the depth of the tree, 
# while breadth-first traversal uses memory proportional to the breadth of the tree 
# (how many nodes there are on the "level" that has the most nodes).

# Because the tree's breadth can as much as double each time it gets one level deeper, 
# depth-first traversal is likely to be more space-efficient than breadth-first traversal, 
# though they are strictly both O(n)O(n) additional space in the worst case. The space savings 
# are obvious if we know our binary tree is balanced—its depth will be O(\lg{n})O(lgn) and its 
# breadth will be O(n) O(n).

# We do a depth-first walk through the tree, testing each node for validity as we go. 
# A given node is valid if it's greater than all the ancestral nodes it's in the right 
# sub-tree of and less than all the ancestral nodes it's in the left-subtree of. 
# Instead of keeping track of each ancestor to check these inequalities, we just check the 
# largest number it must be greater than (its lower_bound) and the smallest number it must be 
# less than (its upper_bound).


# Complexity: O(n) space, time
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

def valid_tree(root):

  # Start with the root, with an arbitrary low bound and upper bound
  nodes_and_bounds_stack = [(root, -float('inf'), float('inf'))]

  # DFS traversal
  while len(nodes_and_bounds_stack):
    node, lower_bound, upper_bound = nodes_and_bounds_stack.pop()

    # If node is invalid, we return false right away
    if node.value <= lower_bound or node.value >= upper_bound:
      return False

    if node.left:
      # this node must be less than the current node
      nodes_and_bounds_stack.append((node.left, lower_bound, node.value))
    if node.right:
      # this node must be greater than current node
      nodes_and_bounds_stack.append((node.right, node.value, upper_bound))

  # At this point we have checked all nodes, return valid
  return True
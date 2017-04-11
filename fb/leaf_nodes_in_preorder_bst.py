# Given a pre-order traversal, determine how many
# leaf nodes there are without building the tree.

# Idea: any time the value increases, the value that is
#       smaller is a leaf node.

def preorderLeaves(arr):
  num_leaves = 0
  length = len(arr)
  for i in xrange(0, length):
    if i == 0:
      pass
    elif i == length - 1:
      num_leaves += 1
    elif arr[i] < arr[i + 1]:
      num_leaves += 1
  return num_leaves

print preorderLeaves([5, 3, 2, 4, 8, 7, 9])
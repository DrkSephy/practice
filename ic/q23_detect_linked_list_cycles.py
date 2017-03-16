class LinkedListNode:

  def __init__(self, value):
      self.value = value
      self.next  = None

# A cycle occurs when a node’s next points back to a previous node in the list. 
# The linked list is no longer linear with a beginning and end—instead, it cycles 
# through a loop of nodes.

# Write a function contains_cycle() that takes the first node in a singly-linked 
# list and returns a boolean indicating whether the list contains a cycle.

# We could use a set to find the duplicate visited nodes, but that is O(n) space.

# We can do better, using two pointers and start them at the head.
# The first "runner" moves forward once, while the second "runner" moves forward twice.
# If the list has a cycle, the second runner will lap the first runner.

def contains_cycle(first_node):

  # Start both pointers at the beginning
  slow_runner = first_node
  fast_runner = first_node

  # Until we hit the end of the list
  while fast_runner is not None and fast_runner.next is not None:
    slow_runner = slow_runner.next
    fast_runner = fast_runner.next.next

    # case: fast_runner is about to lap slow runner
    if fast_runner is slow_runner:
      return True

  # Case: fast_runner hit the end of the list
  return False

# Complexity: O(n) time, O(1) space
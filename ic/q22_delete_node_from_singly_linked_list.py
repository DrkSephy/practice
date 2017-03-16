# Delete a node from a singly-linked list, 
# given only a variable pointing to that node.

# Since we don't have a reference to the head,
# We copy the value of the next node to the 
# reference node to delete, then delete it's
# next node.


class LinkedListNode:

  def __init__(self, value):
      self.value = value
      self.next  = None

def delete_node(node_to_delete):
  # Get the input's next node, the one we want to skip to
  next_node = node_to_delete.next

  if next_node:
    # Replace the input node's value and pointer 
    # with the next node's value and pointer. The previous
    # node now effectively skips over the input node
    node_to_delete.value = next_node.value
    node_to_delete.next = next_node.next

  else:
    # cannot delete last node
    raise Exception('Cannot delete last node')

# There are two potential side-effects:

# 1. Any references to the input node have now effectively been reassigned to its next node. 
#    In our example, we "deleted" the node assigned to the variable b, but in actuality we just 
#    gave it a new value (2) and a new next! If we had another pointer to b somewhere else in our 
#    code and we were assuming it still had its old value (8), that could cause bugs.

# 2. If there are pointers to the input node's original next node, those pointers now point to a 
#    "dangling" node (a node that's no longer reachable by walking down our list). In our example 
#    above, c is now dangling. If we changed c, we'd never encounter that new value by walking down 
#    our list from the head to the tail.
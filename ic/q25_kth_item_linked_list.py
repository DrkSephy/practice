# Write a function kth_to_last_node() that takes an integer k and 
# the head_node of a singly linked list, and returns the kth to 
# last node in the list.

# Solution 1: O(n) runtime, O(1) space
def kth_to_last_node(k, head):

  # STEP 1: get the length of the list
  # start at 1, not 0
  # else we'd fail to count the head node!
  list_length = 1
  current_node = head

  # traverse the whole list,
  # counting all the nodes
  while current_node.next:
      current_node = current_node.next
      list_length += 1

  # STEP 2: walk to the target node
  # calculate how far to go, from the head,
  # to get to the kth to last node
  how_far_to_go = list_length - k

  current_node = head
  for i in xrange(how_far_to_go):
      current_node = current_node.next

  return current_node
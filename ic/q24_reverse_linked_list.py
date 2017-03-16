# Reverse a singly linked list, returning the new head

# Solution: We change the pointers for next to be the previous node.

def reverse(head_of_list):
  current = head_of_list
  previous = None
  next = None

  # until we get to the end of the list
  while current:
    # copy a pointer to the next element
    # before we overwrite current.next
    next = current.next

    # Reverse the next pointer
    current.next = previous

    # Step forward in the list
    prev = current
    current = next
  return previous

# Complexity: O(n) time, O(1) space. We pass over the list once.


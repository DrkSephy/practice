# Find the kth to last element of a linked list.

class Node(object):

  def __init__(self, data, next=None):
      self.next = next
      self.data = data

  def __str__(self):
      return self.data


class LinkedList(object):

  def __init__(self, head=None):
      self.head = head

  def __len__(self):
      curr = self.head
      counter = 0
      while curr is not None:
          counter += 1
          curr = curr.next
      return counter

  def insert_to_front(self, data):
      if data is None:
          return None
      node = Node(data, self.head)
      self.head = node
      return node

  def append(self, data):
      if data is None:
          return None
      node = Node(data)
      if self.head is None:
          self.head = Node(data)
          return node
      curr_node = self.head
      while curr_node.next is not None:
          curr_node = curr_node.next
      curr_node.next = node
      return node

  def find(self, data):
      if data is None:
          return None
      curr_node = self.head
      while curr_node is not None:
          if curr_node.data == data:
              return curr_node
          curr_node = curr_node.next
      return None

  def delete(self, data):
      if data is None:
          return
      if self.head is None:
          return
      if self.head.data == data:
          self.head = None
          return
      prev_node = self.head
      curr_node = self.head.next
      while curr_node is not None:
          if curr_node.data == data:
              prev_node.next = curr_node.next
              return
          prev_node = curr_node
          curr_node = curr_node.next

  def delete_alt(self, data):
      if data is None:
          return
      if self.head is None:
          return
      curr_node = self.head
      if curr_node.data == data:
          curr_node = curr_node.next
          return
      while curr_node.next is not None:
          if curr_node.next.data == data:
              curr_node.next = curr_node.next.next
              return
          curr_node = curr_node.next

  def print_list(self):
      curr_node = self.head
      while curr_node is not None:
          print(curr_node.data)
          curr_node = curr_node.next

  def get_all_data(self):
      data = []
      curr_node = self.head
      while curr_node is not None:
          data.append(curr_node.data)
          curr_node = curr_node.next
      return data

  def get_kth_to_last_element(self, k):
    if self.head is None:
      return None
    fast = self.head
    slow = self.head

    # Give fast a headstart, incrementing it
    # once for k=1, for k=2,etc
    for _ in range(k):
      fast = fast.next
      # If k >= num elements, return None
      if fast is None:
        return None

    # Increment both pointers until fast reaches the end
    while fast.next is not None:
      fast = fast.next
      slow = slow.next
    return slow.data

  def get_kth_to_last_element_two(self, k):
    # Get length of the list
    if self.head is None:
      return None

    length = 1
    pointer = self.head
    while pointer.next is not None:
      pointer = pointer.next
      length += 1
    print 'length of list: ', length

    # Iterate through the list up to length - k
    pointer = self.head
    print 'Starting at: ', pointer.data
    for _ in xrange(length - k - 1):
      pointer = pointer.next
    return pointer.data

  def is_palindrome(self):
    if self.head is None or self.head.next is None:
      return False
    curr = self.head
    reversed_list = LinkedList()
    length = 0

    # Reverse the linked list
    while curr is not None:
      reversed_list.insert_to_front(curr.data)
      length += 1
      curr = curr.next

    reversed_list.print_list()


    # Compare the reversed list with the original list
    # Only need to compare the first half
    iterations = length // 2
    print '---only need this many iterations', iterations
    curr = self.head
    curr_reversed = reversed_list.head
    for _ in range(iterations):
      if curr.data != curr_reversed.data:
        return False
      curr = curr.next
      curr_reversed = curr_reversed.next
    return True

  def partition(self, data):
    # Create a linked list to store the left data
    left = LinkedList(None)

    # Create a linked list to store the right data
    right = LinkedList(None)

    curr = self.head
    # Iterate over the original list
    while curr is not None:
      if curr.data < data:
        left.append(curr.data)
      elif curr.data == data:
        right.insert_to_front(curr.data)
      else:
        right.append(curr.data)
      curr = curr.next
    curr_left = left.head
    # Is the left list empty?
    if curr_left is None:
      return right
    else:
      # merge two lists
      while curr_left.next is not None:
        curr_left = curr_left.next
      curr_left.next = right.head
      return left

  def remove_dupes(self):
    if self.head is None:
        return
    node = self.head
    seen_data = set({node.data})
    while node.next is not None:
      if node.next.data in seen_data:
        node.next = node.next.next
      else:
        seen_data.add(node.next.data)
        node = node.next
    self.print_list()

head = Node(2)
linked_list = LinkedList(head)
linked_list.append(1)
linked_list.append(3)
linked_list.append(10)
linked_list.append(7)
linked_list.append(2)
linked_list.append(3)
# linked_list.print_list()

# List is 2 -> 1 -> 3 -> 5 -> 7
# print linked_list.get_kth_to_last_element(2)
# print linked_list.get_kth_to_last_element_two(2)


# PROBLEM
# Determine if a Linked List is a Palindrome
# Reverse the list
#  - iterate through the current linked list
#  - insert to front the current node into a new linked list
# Compare the reversed list with the original list
#   - only need to compare the first half

# linked_list.print_list()
# print linked_list.is_palindrome()

# PROBLEM
# Partition a list around a node X, such that 
# all nodes less than X are on the left, and all 
# nodes greater than X are on the right.
# partitioned_list = linked_list.partition(5)
# print partitioned_list.get_all_data()

# PROBLEM
# Remove all duplicates from a Linked List
# linked_list.print_list()
linked_list.remove_dupes()

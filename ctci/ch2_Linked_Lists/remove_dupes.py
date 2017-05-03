# Write code to remove duplicates from an unsorted linked list.

class Node(object):

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList(object):
  
  head = None
  tail = None

  def show(self):
    x = self.head
    repr = ''
    while x is not None:
      repr += str(x.data) + ' -> '
      x = x.next
    print repr + 'None'

  def append(self, data):
    new_node = Node(data, None)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def remove(self, node_value):
    prev = None
    x = self.head
    while x is not None:
      if x.data == node_value:
        # Is there a previous node? Link it to the next node
        if prev is not None:
          prev.next = x.next
        else:
          self.head = x.next
        break
      else:
        prev = x
        x = x.next
    if x.next is None:
      self.tail = x
    if self.head is None:
      self.tail = None

  def is_empty(self):
    return self.head is None

  # This uses temporary storage (hash set)
  # O(n) space, O(n) time
  def remove_duplicates(self):
    hash = set()
    x = self.head
    prev = None
    while x is not None:
      # Is x.data in our hash set already?
      if x.data in hash:
        # We need to jump over this node
        prev.next = x.next
      else:
        hash.add(x.data)
        prev = x
      x = x.next

  # Follow up: can you do this without temporary space?
  def remove_duplicates_without_aux(self):
    x = self.head
    runner = x
    while x is not None:
      while runner.next is not None:
        if x.data == runner.next.data:
          runner.next = runner.next.next
        else:
          runner = runner.next
      x = x.next
      runner = x

  # 2.3: Delete middle node. Implement an algorithm to delete a node in the middle
  # (i.e, any node but the first and last node, not necessarily in the middle) of a
  # singly linked list, given only access to that node.
  def remove_middle_node(self, node):
    if node is None or node.next is null:
      return false

    # Approach: Copy next node data into current node to remove, and remove the next node
    new_node = node.next
    node.data = new_node.data
    node.next = new_node.next
    return true;

  # 2.4: Partition. Write code to partition a linked list around a value x, such that all
  # nodes less than x come before all nodes greater than or equal to x. If x is contained
  # within the list, the values of x only need to be after the elements less than x.
  # The partition element x can appear anywhere in the "right partition", it does not 
  # need to appear between the left and right partitions.
  # Example:
  #   INPUT: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
  #   OUTPUT: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

  # Approach: split the linked list into two separate lists. One list (left list)
  # will contain all the values less than partition value. Second list (right list)
  # will contain all values >= the partition value.
  def partition_list(self, partition_value):
    left_list = []
    right_list = []
    # Loop over linked list, checking values
    curr = self.head
    while curr is not None:
      if curr.data < partition_value:
        left_list.append(curr.data)
      else:
        right_list.append(curr.data)
      curr = curr.next
    print left_list + right_list
    return







if __name__ == "__main__":
  ll = LinkedList()
  ll.append(3)
  ll.append(5)
  ll.append(8)
  ll.append(5)
  ll.append(10)
  ll.append(2)
  ll.append(1)
  ll.partition_list(5)
  # ll.show()
  # ll.remove_duplicates()
  # ll.remove_duplicates_without_aux()
  # ll.show()
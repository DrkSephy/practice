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

  # 2.2: kth to last
  # Implement an algorithm to print the kth to last element
  # in a singly linked list.

  # O(1) space, O(n) time
  def kth_to_last(self, k):
    # step 1: get length of list
    len = 0
    x = self.head
    while x is not None:
      len += 1
      x = x.next
    
    # step 2: move len - k steps
    x = self.head
    for _ in xrange(len - k):
      x = x.next
    print x.data


if __name__ == "__main__":
  s = LinkedList()
  s.append(31)
  s.append(2)
  s.append(3)
  s.append(4)
  s.kth_to_last(2)
  # s.show()
  # s.remove(31)
  # s.show()
  # s.remove(3)
  # s.remove(2)
  # s.show()
  # s.append(5)
  # s.append(3)
  # s.append(31)
  # s.append(2)
  # s.show()

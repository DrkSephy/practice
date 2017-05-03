class Node(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Queue(object):
  def __init__(self, first=None, last=None):
    self.first = first
    self.last = last

  def add(self, item):
    new_node = Node(item)
    if self.last is not None:
      self.last.next = new_node
    self.last = new_node

    if self.first is None:
      self.first = self.last

  def remove(self):
    if self.first is None:
      raise IndexError('There is nothing in the queue')
    
    # Grab front of list
    node = self.first.data
    
    # Make next node the first node
    self.first = self.first.next
    
    # Is self.first now None? i.e, was this the only item in the list?
    if self.first is None:
      self.last = None

    return node

  def peek(self):
    if self.first is None:
      raise IndexError('There is nothing in the queue')
    return self.first.data

  def isEmpty(self):
    return self.first is None

q = Queue()
q.add(5)
q.add(6)
q.add(7)
print q.remove()
print q.remove()
print q.add(10)
q.remove()
print q.peek()
q.remove()
print q.isEmpty()



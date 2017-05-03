class Node(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack(object):
  def __init__(self, top=None):
    self.top = top

  def pop(self):
    if not self.top:
      return None
    data = self.top.data
    self.top = self.top.next
    return data

  def push(self, item):
    new_node = Node(item)
    new_node.next = self.top
    self.top = new_node

  def peek(self):
    if not self.top:
      return None
    return self.top.data

  def isEmpty(self):
    return self.top is None


# Initialize stack
# s = Stack()

# # Push some numbers
# s.push(5)
# s.push(3)
# s.push(2)

# # Pop some numbers
# print s.pop()
# print s.pop()
# print s.pop()
# print s.peek()
# print s.isEmpty()



# 3.2: Stack min. How would you design a stack which, in addition to push and pop, has a function
# min which returns the minimum element? Push, pop, and min should all operate in O(1) time.

# Approach: Use an auxillary stack to store mins
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

class StackWithMin(object):
  def __init__(self):
    self.stack = Stack()
    self.min_stack = Stack()

  def push(self, value):
    # Check if top of min stack exists, and value < top of min stack
    if value < self.min():
      self.min_stack.push(value)
    self.stack.push(value)

  def min(self):
    if self.min_stack.isEmpty():
      return float('inf')
    else:
      return self.min_stack.peek()

  def pop(self):
    value = self.stack.pop()
    # print value, self.min()
    if value == self.min():
      # print 'Equal value'
      self.min_stack.pop()
    return value

# Initialize stackWithMin
swm = StackWithMin()
swm.push(5)
swm.push(3)
print swm.min() # 3
swm.pop()
print swm.min()
swm.push(0)
print swm.min()




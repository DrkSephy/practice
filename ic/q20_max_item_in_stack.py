class Stack:

  # initialize an empty list
  def __init__(self):
    self.items = []

  # push a new item to the last index
  def push(self, item):
    self.items.append(item)

  # remove the last item
  def pop(self):
    # if the stack is empty, return None
    # (it would also be reasonable to throw an exception)
    if not self.items:
        return None
    return self.items.pop()

  # see what the last item is
  def peek(self):
    if not self.items:
        return None
    return self.items[-1]

# Use your Stack class to implement a new class MaxStack with a 
# function get_max() that returns the largest element in the stack. 
# get_max() should not remove the item. Your stacks will contain only integers.

# Easiest solution would be to have get_max() simply walk through the stack
# to find the max element, taking O(n) time. We can do it in O(1) time.

# For every push(), we can check to see if the item being pushed is larger 
# than the current max, assigning it as our new max if so. But what happens 
# when we pop() the current max? We could re-compute the current max by walking 
# through our stack in O(n)O(n) time. So our worst-case runtime for pop() would be 
# O(n). We can do better.

# What if when we find a new current max (new_max), instead of overwriting the old 
# one (old_max) we held onto it, so that once new_max was popped off our stack we would 
# know that our max was back to old_max?

# What data structure should we store our set of maxs in? We want something where the 
# last item we put in is the first item we get out ("last in, first out").

# Solution: define two new stacks within our MaxStack class - stack holds all our integers, 
# and max_stack holds our "maxima". We use max_stack to keep our max up to date in constant 
# time as we push() and pop():

# 1. Whenever we push() a new item, we check if it is greater than or equal to the current max,
#    which is at the top of maxs_stack. If it is, we also push() it onto maxs_stack.
# 2. Whenever we pop(), we also pop() from the top of maxs_stack if the item equals the top item in
#    maxs_stack.

class MaxStack:

  def __init__(self):
    self.stack      = Stack()
    self.maxs_stack = Stack()

  # Add a new item to the top of our stack. If the item is greater,
  # than or equal to the last item in maxs_stack, its the new max!
  # So we'll add it to maxs_stack.
  def push(self, item):
    self.stack.push(item)
    if self.maxs_stack.peek() is None or item >= self.maxs_stack.peek():
      self.maxs_stack.push(item)

  # Remove and return the top item from our stack. If it equals
  # the top item in maxs_stack, they must have been pushed in together.
  # So we'll pop it out of maxs_stack too.
  def pop(self):
    item = self.stack.pop()
    if item == self.maxs_stack.peek():
      self.maxs_stack.pop()
    return item

  # The last item in maxs_stack is the max item in our stack
  def get_max(self):
    return self.maxs_stack.peek()

# Complexity of solution: O(1) time for push(), pop(), and get_max(). O(m) additional
# space, where m is the number of operations performed on the stack.
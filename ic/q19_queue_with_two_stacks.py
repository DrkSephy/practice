# Implement a queue with 2 stacks. Your queue should have an 
# enqueue and a dequeue function and it should be "first in first out" (FIFO).
# Optimize for the time cost of m function calls on your queue. 
# These can be any mix of enqueue and dequeue calls.

# Assume you already have a stack implementation and it gives O(1) O(1) time push and pop.

class QueueTwoStacks:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []

    def enqueue(self, item):
      self.in_stack.append(item)

    def dequeue(self):
      if len(self.out_stack) == 0:
        # Move items from in_stack to out_stack, reversing order
        while len(self.in_stack) > 0:
          newest_in_stack_item = self.in_stack.pop()
          self.out_stack.append(newest_in_stack_item)

        # if out_stack is still empty
        if (len(self.out_stack) == 0):
          raise IndexError('Cannot dequeue from empty queue')
      return self.out_stack.pop()

# Complexity: O(m) time
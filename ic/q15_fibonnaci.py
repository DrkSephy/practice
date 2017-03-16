# Write a function fib() that a takes an integer n 
# and returns the nth fibonacci number.

# Need to memoize past computations
memo = {}

# Regular fibonacci numbers with recursion is O(2^n).
# Using memoization, O(n) runtime, O(n) space.
def fib(n):
  # base case: n is 1 or 0
  if n in [1, 0]:
    return n

  # Check if we computed this before
  if n in memo:
    return memo[n]

  result = fib(n - 1) + fib(n - 2)
  
  # Save results
  memo[n] = result
  return result

# We can do this in constant space. Recursion can overflow
# the call stack, how about a bottom up approach?

def fib_bottom_up(n):
  if n in [1, 0]:
    return n

  prev_prev = 0 # 0th fib
  prev = 1 # 1st fib

  for i in range(n - 1):
    # To get nth fib, go up to n - 1
    current = prev + prev_prev
    prev_prev = prev
    prev = current
  return current

print fib_bottom_up(100)

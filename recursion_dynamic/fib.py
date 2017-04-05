# Implement fibonacci numbers recursively, dynamically, iteratively.

def fib_iterative(n):
  a = 0
  b = 1
  for _ in range(n):
    a, b = b, a + b
  return a

def fib_recursive(n):
  if n in [0, 1]:
    return n
  else:
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_dynamic(n):
  memo = {}
  return _fib_dynamic(n, memo)

def _fib_dynamic(n, memo):
  if n in [0, 1]:
    return n

  if n in memo:
    return memo[n]

  memo[n] = _fib_dynamic(n - 1, memo) + _fib_dynamic(n - 2, memo)
  return memo[n]


# Test Iterative fib
print fib_iterative(6)

# Test Recursive fib
print fib_recursive(6)

# Test dynamic fib
print fib_dynamic(6)
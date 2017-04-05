# You are running up n steps. If you take a single, 
# double, or triple step, how many possible ways
# are there to run up to the nth step?

def count_ways(num_steps):
  if num_steps is None or num_steps < 0:
    raise TypeError('num_steps cannot be None or negative')

  memo = {}
  return _count_ways(num_steps, memo)

def _count_ways(num_steps, memo):
  if num_steps < 0:
    return 0

  if num_steps == 0:
    return 1

  if num_steps in memo:
    return memo[num_steps]

  memo[num_steps] = (_count_ways(num_steps - 1, memo) + _count_ways(num_steps - 2, memo) + _count_ways(num_steps - 3, memo))
  print memo
  return memo[num_steps]

print count_ways(10)
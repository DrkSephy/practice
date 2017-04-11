# A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps
# at a time. Impleent a method to count how many possible ways the child can run up the stairs.

# num_steps: number of steps to climb
# steps: array of steps the child can take
def stairs(num_steps, steps):
  # Store a 1D array of how many ways the child can climb each step
  tally = [1] + [0] * num_steps

  # Loop over each step the child can take
  for step in steps:
    for i in range(step, num_steps + 1):
      tally[i] += tally[i - step]
      print tally, 'i: ', i
  return 0 if num_steps == 0 else tally[num_steps]


# print stairs(5, [1, 2, 3])


def recurse_stairs(num_steps):
  if num_steps < 0:
    return 0
  elif num_steps == 0:
    return 1
  else:
    return recurse_stairs(num_steps - 1) + recurse_stairs(num_steps - 2) + recurse_stairs(num_steps - 3)

print recurse_stairs(5)

# def Method2(x):
#   memo = [-1] * (x + 1)
#   return TripleHopRecursive(x, memo)


# def TripleHopRecursive(x, memo):
#   if x < 0:
#       return 0
#   memo[0] = 1
#   if x >= 1:
#       memo[1] = 1
#   if x >= 2:
#       memo[2] = memo[1] + memo[0]
#   if x > 2:
#       for i in range(3, x + 1):
#           memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
#   print memo
#   return memo[x]

# print Method2(5)
# Given a list of tuples of start/end times,
# determine the number of time covered by the intervals.

# i.e: input -> [(1, 4), (2, 3)] = 3
# input -> [(4, 6), (1, 2)] = 3
# input -> [(1, 4), (6, 8), (2, 4), (7, 9), (10, 15)] = 11

# [(1, 4), (2, 4), (6, 8), (7, 9), (10, 15)]

def interval(arr):
  arr.sort()
  ending = 0
  ans = 0
  time = 0
  for val in arr:
    ans += max(val[1] - max(val[0], ending), 0);
    ending = max(ending, val[1])

  return ans

# print interval([(4, 6), (1, 2)])
print interval([(1, 4), (6, 8), (2, 4), (7, 9), (10, 15)])
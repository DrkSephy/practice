# Given a sequence of positive integers A
# and an integer T, return whether there
# is a continuous sequence of A that sums up 
# to exactly T.

def continuous_sum(arr, target):
  start = 0
  end = 1
  while start != len(arr) - 1:
    # Use sliding window. If sum > target, move left cursor right.
    # If sum < target, move end cursor right.
    if sum(arr[start:end]) == target:
      print arr[start:end]
      return True
    elif sum(arr[start:end]) > target:
      start += 1
    elif sum(arr[start:end]) < target:
      end += 1
  return False

print continuous_sum([23, 5, 4, 7, 2, 11], 20) # True, [7, 2, 11]
print continuous_sum([1, 3, 5, 23, 2], 8) # True, [3, 5]
print continuous_sum([1, 3, 5, 23, 2], 7) # False
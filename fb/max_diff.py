# Given an array, find the maximum difference between two
# array elements, given the second element comes after the
# last.

def max_diff(arr):
  minimum = arr[0]
  diff = 0
  for index, val in enumerate(arr):
    if index == 0:
      pass
    
    potential_diff = val - minimum
    diff = max(diff, potential_diff)
    minimum = min(minimum, val)
  return diff

print max_diff([65, 7, 5, 9, 8, 2, 10, 15, 19])
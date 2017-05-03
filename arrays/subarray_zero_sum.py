# Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.

# Input: {4, 2, -3, 1, 6}
# Output: true 
# There is a subarray with zero sum from index 1 to 3.

# Input: {4, 2, 0, 1, 6}
# Output: true 
# There is a subarray with zero sum from index 2 to 2.

def subarray(arr):
  memo = {}
  sum = 0
  for val in arr:
    sum += val
    print sum
    if sum == 0 and memo[sum]:
      return True
    memo[sum] = True
  print memo
  return False

print subarray([4, 2, -3, 1, 6])

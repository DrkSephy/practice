# Given an array of positive, unique, increasingly 
# sorted numbers A = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13].
# Given a positive value K = 3, output all pairs of 
# numbers in A that differ exactly by K.

def pairs(arr):
  start = 0
  end = 1
  pairs = []
  for i in range(0, len(arr)):
    # Check if values at index {start, end} has equal diff
    if arr[end] - arr[start] == 3:
      pairs.append((arr[start], arr[end]))
      # Move start, end forward by 1
      start += 1
      end += 1
    # Check if difference is too low. If so, move end to the right
    elif arr[end] - arr[start] < 3:
      end += 1
    elif arr[end] - arr[start] > 3:
      start += 1
  return pairs



A = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]
print pairs(A)
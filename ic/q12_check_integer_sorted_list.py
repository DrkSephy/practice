# Suppose we had a list of n integers sorted in ascending order. 
# How quickly could we check if a given integer is in the list?

# We can use binary search O(log n) time, O(1) space to find an integer
# in an ascending sorted list

def binary_search(sequence, value):
  lo, hi = 0, len(sequence) - 1 # 0, 4
  while lo <= hi: # -> 3 < 4, -> 4 <= 4
      mid = (lo + hi) // 2 #  mid is now = 3 + 4 // 2 = 7 // 2 = 3
      if sequence[mid] < value: # 8 < 10, 9 < 10
          lo = mid + 1 # lo = 2 + 1 -> 3, lo = 3 + 1 = 4
      elif value < sequence[mid]:
          hi = mid - 1
      else:
          return mid # finally, sequence[4] == 10, our value. return mid
  return None

print binary_search([1, 5, 8, 9, 10], 10)






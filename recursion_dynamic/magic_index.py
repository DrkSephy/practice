# Find the magic index in a sorted array, where array[i] = i

# Simple method is O(n) time, O(n) space where we 
# linearally scan items in the array.

# We can do this in O(log n) time and space with a modified
# binary search.

# 1. Compute mid
# 2. If mid == array[mid], return mid
# 3. Otherwise, if recurse on left side if mid < array[mid]
# 4. Else, recurse on right side if mid > array[mid]

def find_magic_index(seq, start = None, end = None):
  if start is None:
        start = 0

  if end is None:
      end = len(array) - 1

  if start > end:
      return -1

  index = (start + end) // 2
  value = seq[index]

  if index == value:
    return index

  # Left sub-array
  left_end = min(index - 1, value)
  left_index = find_magic_index(seq, start=start, end=left_end)
  if left_index != -1:
    return left_index

  # Right sub-array
  right_start = max(index + 1, value)
  return find_magic_index(seq, start=right_start, end=end)


print find_magic_index([-4, -2, 2, 6, 6, 6, 6, 10], 0, len([-4, -2, 2, 6, 6, 6, 6, 10]) - 1) # returns 2
print find_magic_index([-4, -2, 1, 6, 6, 6, 6, 10], 0, len([-4, -2, 1, 6, 6, 6, 6, 10]) - 1) # returns 6

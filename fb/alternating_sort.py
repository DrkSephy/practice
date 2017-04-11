# Given an unsorted array, sort it in such a way
# that the first element is the largest value,
# the second element is the smallest, 
# the third element is the second largest, and so on.

# Can you do it in less than n^2 time with O(1) space?

def alternateSort(arr):
  # Sort array in place, n log n
  arr.sort()

  # Do in-place swap
  start = 0
  end = len(arr) - 1
  alternate = True
  while start <= end:
    if start == end:
      end += 1
    print start, end
    arr[start], arr[end] = arr[end], arr[start]
    if alternate:
      start += 1
      alternate = False
    else:
      end -= 1
      start += 1
      alternate = True
    print arr
  print arr


print alternateSort([2, 4, 3, 5, 1, 6])
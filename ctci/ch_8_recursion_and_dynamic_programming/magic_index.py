# Given a sorted array, find the magic index where index == value.

def magicRecurse(arr):
  return magicRecurseDupes(arr, 0, len(arr))

def magicRecurseFind(arr, start, end):
  if end < start:
    return -1

  # Find midpoint
  mid = (start + end) // 2

  # Check if mid index is magic index
  if arr[mid] == mid:
    return mid
  # If value at mid is greater than mid index, magic index
  # must lie to the left
  elif arr[mid] > mid:
    return magicRecurseFind(arr, start, mid -1)
  else:
    return magicRecurseFind(arr, mid + 1, end)

# print magicRecurse([-40, -20, -1, 1, 2, 3, 5, 7, 7, 9, 12, 13])

# Handle case where elements are not distinct
def magicRecurseDupes(arr, start, end):
  if end < start:
    return -1

  midIndex = (start + end) // 2
  midValue = arr[midIndex]
  if midValue == midIndex:
    return midIndex

  # Search the left
  leftIndex = min(midIndex - 1, midValue)
  print 'LeftIndex', leftIndex
  left = magicRecurseDupes(arr, start, leftIndex)
  if left >= 0:
    return left

  # Search the right
  rightIndex = max(midIndex + 1, midValue)
  print 'RightIndex', rightIndex
  right = magicRecurseDupes(arr, rightIndex, end)
  return right

print magicRecurse([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13])

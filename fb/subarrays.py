# Given an array, split it into subarrays that are sorted
# in ascending order.

# Ex: [1, 5, 7, 2, 6, 10, 3, 8, 11] -- > [[1, 5, 7], [2, 6, 10], [3, 8, 11]]

def partition(arr):
  subsets = []
  subset = []
  for index, val in enumerate(arr):
    if index == 0:
      subset.append(val)
      continue

    # Is the current element greater than the previous? If so, add it to the current subset
    if val > arr[index - 1] :
      subset.append(val)

    # Is the current element less than the previous? If so, add the current subset into subsets
    # and start building a new subset
    if val < arr[index - 1]:
      # Push the subset we were building
      subsets.append(subset)
      # Empty the subset we were building, push current value in
      subset = []
      subset.append(val)

    # Is the current element equal to the previous? If so, add it to the current subset
    if val == arr[index - 1]:
      subset.append(val)

    # Are we looking at the last element?
    if index == len(arr) - 1:
      subsets.append(subset)
  return subsets

print partition([1, 5, 7, 2, 6, 10, 3, 8, 11])
print partition([1, 5, 7, 2, 6, 10, 3, 8, 11, 10])
print partition([5, 4, 3, 1])

def sort_partitions(partitions):
  
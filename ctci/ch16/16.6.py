# Smallest Difference: Given two arrays of integers, compute the pair of values
# (one value in each array) with the smallest (non-negative) difference. Return the difference.

# Example:
# Input: [1, 3, 15, 11, 2], [23, 127, 235, 19, 8]
# Output: 3. Pair: [11, 8]

# O(AB) time
def smallest_difference(arr1, arr2):
  if len(arr1) == 0 or len(arr2) == 0:
    return -1

  min_value = float('inf')
  for i in range(len(arr1)):
    for j in range(len(arr2)):
      if abs(arr1[i] - arr2[j]) < min_value:
        min_value = abs(arr1[i] - arr2[j])
  return min_value


# print smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])


# O (A log A + B log B) runtime, O(1) space
def smallest_distance_log(arr1, arr2):
  if len(arr1) == 0 or len(arr2) == 0:
    return -1

  arr1 = sorted(arr1)
  arr2 = sorted(arr2)

  index_one = 0
  index_two = 0

  difference = float('inf')
  while(index_one < len(arr1) and index_two < len(arr2)):
    if abs(arr1[index_one] - arr2[index_two]) < difference:
      difference = abs(arr1[index_one] - arr2[index_two])

    # Move forward in the array with the smaller value
    if arr1[index_one] < arr2[index_two]:
      index_one += 1
    else:
      index_two += 1
  return difference

print smallest_distance_log([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])


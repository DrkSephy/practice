# Given two sorted arrays, return a single sorted array 
# with values from both arrays.

# Ex:
#    Array 1: [3, 4, 6, 10, 11, 15]
#    Array 2: [1, 5, 8, 12, 14, 19]
# Return: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]


# O(n) space, O(n) time
def merge_sorted_arrays(arr1, arr2):
  # Store index of array 1
  arr_one_index = 0

  # Store index of array 2
  arr_two_index = 0

  # Store length of array 1
  arr_one_parity = len(arr1)

  # Store length of array 2
  arr_two_parity = len(arr2)

  # New array to return
  sorted_arr = []

  # Loop over both arrays, stepping forward based on values
  while True:
    # Compare values at indexes
    # Is the value at index in arr1 greater than in arr2?
    if arr1[arr_one_index] < arr2[arr_two_index]:
      # If it is smaller, push it into our sorted array
      sorted_arr.append(arr1[arr_one_index])

      # Make sure we don't step forward out of bounds in array 1
      if arr_one_index + 1 < arr_one_parity:
        # Step forward in array 1
        arr_one_index += 1
      # If we've finished processing array one, concat both arrays
      else:
        sorted_arr.extend(x for x in arr2[arr_two_index:])
        break

    # Array 2 has a lower value than Array 1
    else:
      sorted_arr.append(arr2[arr_two_index])
      # Make sure we don't step out of bounds in array 2
      if arr_two_index + 1 < arr_two_parity:
        # Step forward in array 2
        arr_two_index += 1
      else:
        # We finished array 2, push everything from array 1
        sorted_arr.extend(x for x in arr1[arr_one_index:])
        break
  return sorted_arr

print merge_sorted_arrays([1, 2, 3, 8, 10, 15], [4, 5, 6, 7])



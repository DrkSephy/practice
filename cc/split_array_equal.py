# Given an array of integers greater than zero, find if it
# is possible to split it into two arrays (without reordering 
# the inputs) which have the same sum. Print the resulting arrays

def split_arr(arr):
  # Sum the array
  arr_sum = sum(x for x in arr)
  
  # Get end index of array
  index_back = len(arr) - 1
  index_front = 0

  sum1 = 0
  # Walk array backwards and forwards, checking if the two sums ever equal each other
  for idx, val in enumerate(arr):
    sum1 += val
    arr_sum -= val
    if sum1 == arr_sum:
      print arr[0:idx + 1]
      print arr[idx+1:]
  return False

split_arr([1,2,3,4,5,6,21])

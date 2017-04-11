# Given an array of integers greater than zero,
# find if it is possible to split it in 
# two (without reordering the elements)
# such that the sum of the two resulting
# arrays is the same. Print the resulting arrays.

def split_arr(arr):
  arr_sum = sum(arr)
  end = len(arr) - 1
  start = 0
  accum_sum = 0
  # Walk through array
  while start < end:
    # Tally sum from left to right
    accum_sum += arr[start]

    # Decrement total sum from right to left
    arr_sum -= arr[end]
    if accum_sum == arr_sum:
      print start, end
      print arr[0:start -1]
      print arr[start - 1:]
    start += 1
    end -= 1




print split_arr([1,90, 50, 30, 5, 3, 2, 1 ])
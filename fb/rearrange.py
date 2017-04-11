# Given an array of integers,
# 1. Rearrange the array such that all non-zero elements
#    appear on the left of the array.
# 2. Return the number of non-zero members

# e.g. [1,2,0,5,3,0,4,0] => [1,2,5,3,4,0,0,0] and return 5
def rearrange(arr):
  count = 0
  front = 0
  back = len(arr) - 1
  while front < back:
    # Check if front of input is a 0
    if arr[front] == 0:
      # Check for a spot in the back to move it to
      # Is the back a zero?
      if arr[back] == 0:
        # While we keep seeing zeroes...keep moving from right to left
        while arr[back] == 0:
          back -= 1
      else:
        # Swap elements
        arr[back], arr[front] = arr[front], arr[back]
        # Increment non-zero element counter
    else:
      # step forward
      front += 1
      count += 1
  return (count, arr)

def rearrangeTwo(arr):
  x = sorted(arr, reverse=True)
  count = 0
  for val in x:
    if val != 0:
      count += 1
  return count


# print rearrange([1,2,0,5,3,0,4,0,1,2,0,5,3,0,4,0])
print rearrangeTwo([1,2,0,5,3,0,4,0,1,2,0,5,3,0,4,0])

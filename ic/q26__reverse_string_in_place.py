# Reverse a string in place. For Python,
# Convert string into array of chars, perform the 
# in place swap and rejoin the array.

# O(n) time, O(1) space
def in_place_reversal(string):
  string_list = list(string)

  left_pointer = 0
  right_pointer = len(string_list) - 1

  while left_pointer < right_pointer:
    # swap chars
    string_list[left_pointer], string_list[right_pointer] = string_list[right_pointer], string_list[left_pointer]

    # Move towards middle
    left_pointer += 1
    right_pointer -= 1
  # print string_list
  return ''.join(string_list)

print in_place_reversal('hello')

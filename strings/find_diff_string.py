# Find the single different character between two strings.


# Complexity: O(n) space, O(n) time
def find_diff(s1, s2):
  chars = {}

  for char in s1:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1

  for char in s2:
    if char in chars:
      chars[char] -= 1
    else:
      chars[char] = 1

  for key, value in chars.items():
    if value == 1:
      return key

print find_diff('abcd', 'abcde') # --> e
print find_diff('aaabbcdd', 'abdbacade') # --> e


# Complexity: O(n + m) time, O(1) space
def find_diff_xor(str1, str2):
  if str1 is None or str2 is None:
    raise TypeError('str1 or str2 cannot be None')
  result = 0
  for char in str1:
      result ^= ord(char)
  for char in str2:
      result ^= ord(char)
  return chr(result)

print find_diff_xor('abcd', 'abcde') # --> e
print find_diff_xor('aaabbcdd', 'abdbacade') # --> e


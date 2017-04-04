# Determine if two strings are permutations of each other.

# Complexity: O(n) space, O(n) time
def is_permutation(str1, str2):
  chars = {}

  # Store counts of each character in our hash table
  for char in str1:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1

  # For each char in the second string, remove the count if seen
  # Else, add it in
  for char in str2:
    if char in chars:
      chars[char] -= 1
    else:
      chars[char] = 1

  # Check if sum of all counts is 0, meaning the two strings
  # have equal occurrences of characters and are therefore
  # permutations of each other
  total = 0
  for key, value in chars.items():
    total += value

  return True if total == 0 else False


print is_permutation('act', 'cat') # True
print is_permutation('Nib', 'bin') # False
print is_permutation('a ct', 'ca t') # True


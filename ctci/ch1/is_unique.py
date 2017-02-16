# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

import unittest

# O(n) space + time
def unique(string):
  # If length is > 128, there are non ASCII chars inside of it
  if len(string) > 128:
    return False

  chars = [False for x in range(128)]
  for char in string:
    # Ord only works when string is 8 bits
    val = ord(char)

    # Check if value at array position is set to true
    if chars[val]:
      return False # Value at array pos was true, string is not unique

    # Mark position to be true
    chars[val] = True

  # Made it to this point, string is unique
  return True


# O(n log n) time
# O(1) space, we sort array in place. O(n) otherwise
def unique_no_ds(s):
    s.sort() # Sort array of chars in place, n log n
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


class Test(unittest.TestCase):
  true_set = [('abcdefgh'), ('ijklmnop'), ('')]
  false_set = [('aabbcc'), ('ccjjasaoq'), ("1122")]
  true_set_no_ds = [(['a', 'b', 'c', 'd'])]
  false_set_no_ds = [(['a', 'c', 'a'])]

  def test_unique(self):
    # Loop through set of strings that should return True
    for string in self.true_set:
      result = unique(string)
      self.assertTrue(result)

    # Loop through set of strings that should return False
    for string in self.false_set:
      result = unique(string)
      self.assertFalse(result)

  def test_unique_no_ds(self):

    for string in self.true_set_no_ds:
      result = unique_no_ds(string)
      self.assertTrue(result)

    for string in self.false_set_no_ds:
      result = unique_no_ds(string)
      self.assertFalse(result)

if __name__ == "__main__":
  unittest.main()
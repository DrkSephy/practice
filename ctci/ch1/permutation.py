import unittest

# Check permutation: given two strings, write a method to decide
# if one is a permutation of the other.

# O(n) Linear time solution
def is_permutation(s1, s2):
  # If lengths of strings are not equal, cannot be permutations
  if len(s1) != len(s2):
    return False

  map = [0 for x in range(256)] # Assume extended ascii group
  # Loop over each character in string 1, +1 position in map
  # Essentially, we count the occurences of each character
  for char in s1:
    map[ord(char)] += 1

  # Now check each char in string 2, -1 from position in map if found
  # If any value in our map goes to -1, then strings don't have equal
  # character occurences
  for char in s2:
    map[ord(char)] -= 1
    # String 1 has more occurences of char than in String 2
    if map[ord(char)] < 0:
      return False
  return True

class Test(unittest.TestCase):
  true_set = [('abaa', 'baaa')]
  false_set = [('baca', 'ccas')]

  def test_permutation(self):
    for string in self.true_set:
      result = is_permutation(string[0], string[1])
      self.assertTrue(result)

    for string in self.false_set:
      result = is_permutation(string[0], string[1])
      self.assertFalse(result)

if __name__ == "__main__":
  unittest.main()
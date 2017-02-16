# Palindrome Permutation: Given a string, write a function
# to check if it is a permutation of a palindrome. A palindrome
# is a word or phrase that is the same forwards and backards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

import unittest

# Build hash table of character occurances.
# A palindrome needs to have no more than
# one occurence of odd number of characters.
# Etc: {'a': 2, 'b': 1, 'c': 2} can form a palindrome

# - - > O(n) runtime, O(n) space
def checkPermutationPalindrome(string):
  # Build a hash table of character occurences
  hash_table = dict()

  for char in string:
    if char.lower() in hash_table:
      hash_table[char.lower()] += 1
    else:
      hash_table[char.lower()] = 1

  # Boolean to check if we found more than one
  # odd occurence of letters
  foundOddCount = False

  for key, value in hash_table.iteritems():
    # Check if occurence of char is odd
    if value % 2 == 1:
      print key, value
      # Did we already find one odd occurence?
      if foundOddCount:
        # early out, string cannot be permutation of palindrome
        return False
      foundOddCount = True
  return True

class Test(unittest.TestCase):
  true_set = [('abc cba'), ('abcdefg abdecfg')]
  false_set = [('1912010 lkasaal')]

  def test_palindrome_permutation(self):
    for string in self.true_set:
      result = checkPermutationPalindrome(string)
      self.assertTrue(result)

    for string in self.false_set:
      result = checkPermutationPalindrome(string)
      self.assertFalse(result)


if __name__ == "__main__":
  unittest.main()
# Determine if a string S1 is a rotation of another string S2 by 
# Calling (only once) a function is_substring.

# Complexity: O(n) runtime, O(n) space

def is_substring(s1, s2):
  return s1 in s2

def is_rotation(s1, s2):
  if s1 is None or s2 is None:
    return False

  if len(s1) != len(s2):
    return False

  return is_substring(s1, s2 + s2)
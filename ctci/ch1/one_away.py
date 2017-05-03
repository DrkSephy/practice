# There are three types of edits that can be performed on strings:
# Insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# (or zero edits) away.

# Example:
#   pale, ple -> True
#   pales, pale -> True
#   pale, bale -> True
#   pale, bake -> false

def one_away(s1, s2):
  len_diff = len(s1) - len(s2)
  # Are the string lengths different by more than 1 character?
  # If so, they cannot be one edit away from each other
  if len_diff > 1:
    return False
  elif abs(len_diff) == 1:
    if len_diff == -1:
      s1, s2 = s2, s1
    i = 0
    j = 0
    for _ in range(len(s2)):
      # Are the characters in the same position
      # not the same?
      if s1[i] != s2[j] and i == j:
        i += 1
      # both characters are the same in the same index
      elif s1[i] == s2[j]:
        i += 1
        j += 1
      else:
        return False
  # If strings are the same length
  else:
    cnt = 0
    for i in range(len(s1)):
      if s1[i] == s2[i]:
        continue
      elif s1[i] != s2[i]:
        cnt += 1
      if cnt > 1:
        return False
  return True

print one_away('pale', 'ple')
print one_away('pales', 'pale')
print one_away('pale', 'bale')
print one_away('pale', 'bake')

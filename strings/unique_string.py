# Implement an algorithm to determine if a string has all unique characters.

def is_unique(str):
  chars = {}

  for char in str:
    if char in chars:
      return False
    else:
      chars[char] = 1
  return True

print is_unique('bar') # True
print is_unique('foo') # False
print is_unique('') # True
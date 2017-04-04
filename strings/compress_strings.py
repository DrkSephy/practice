from collections import OrderedDict
# Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. 
# Only compress the string if it saves space.

def compress(string):
  chars = OrderedDict()
  for char in string:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  new_string = ''
  print chars
  for key, value in chars.items():
    if value > 1:
      new_string += str(key) + str(value)
    else:
      new_string += str(key)
  return new_string if len(new_string) < len(string) else string


print compress('AABBCC')
print compress('AAABCCDDDD')
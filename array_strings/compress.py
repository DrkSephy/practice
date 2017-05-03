# Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'.
# Only compress the string if it saves space.

def compress_string(string):
  if string is None:
    return None

  hash = {}
  for char in string:
    if char in hash:
      hash[char] += 1
    else:
      hash[char] = 1
  
  compressed = ''
  for key, value in hash.items():
    if value > 1:
      compressed += key + str(value)
    else:
      compressed += key
  
  if len(compressed) != len(string):
    return compressed
  else:
    return string
  

print compress_string('AAABCCDDDD') # A3BC2D4
print compress_string('AABBCC') # AABBCC
print compress_string(None) # None
print compress_string('') # ''
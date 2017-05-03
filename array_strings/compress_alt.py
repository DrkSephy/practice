# Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BCCD4'. 
# Only compress the string if it saves space.

def compress_string_alt(string):
  if string is None or not string:
    return string

  hash = {}
  for char in string:
    if char in hash:
      hash[char] += 1
    else:
      hash[char] = 1

  compressed = ''
  for k, v in hash.items():
    if v > 2:
      compressed += k + str(v)
    else:
      compressed += str(k * v)

  if len(compressed) != len(string):
    return compressed
  else:
    return string

print compress_string_alt('AAABCCDDDD') # A3BCCD4
print compress_string_alt('AABBCC') # AABBCC
print compress_string_alt(None) # None
print compress_string_alt('') # ''
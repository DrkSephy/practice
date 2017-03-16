# Given the list of IDs, which contains many duplicate integers 
# and one unique integer, find the unique integer.

# Brute force way O(n^2) time, O(1) space is to double loop
# over the ids and find the duplicate.

# We can speed this up to O(n) runtime at the cost of O(n) space
# with a dictionary.

def find_unique(list):

  ids = {}

  for id in list:
    if id in ids:
      ids[id] += 1
    else:
      ids[id] = 1

  for id, occurences in ids.items():
    if occurences == 1:
      print ids
      return id

# print find_unique([1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5])

# Can we do it in less than O(n) space?

# We XOR all the integers in the list. We start with a 
# variable unique_delivery_id set to 00. Every time we XOR 
# with a new ID, it will change the bits. When we XOR with the same 
# ID again, it will cancel out the earlier change.

# In the end, we'll be left with the ID that appeared once!

def find_unique_delivery_id(delivery_ids):

  unique_delivery_id = 0

  for delivery_id in delivery_ids:
      unique_delivery_id ^= delivery_id

  return unique_delivery_id

print find_unique_delivery_id([1, 1, 2, 2, 5, 3, 3])
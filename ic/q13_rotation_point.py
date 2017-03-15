# I have a list of words that are mostly alphabetical, except they 
# start somewhere in the middle of the alphabet, reach the end, and 
# then start from the beginning of the alphabet. In other words, this 
# is an alphabetically ordered list that has been "rotated." For example:

#   words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote', # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]

# The set is mostly ordered, we can use binary search to find the rotation point
# words = [ 'k','v','a','b','c','d','e','g','i' ]
#                            ^
# If our "current guess" is the middle item, which is 'c' in this case, 
# is the rotation point to the left or to the right? How do we know?

# Notice that every item to the right of our rotation point is always 
# alphabetically before the first item in the list.

# So the rotation point is to our left if the current item is less than 
# the first item. Else it's to our right.

# Solution:
# We go right if the item we are looking at is greater than the first item
# and go left if the item we are looking at is less than the first item

# When floor_index and ceiling_index are directly next to each other, we know 
# the floor is the last item we added before starting from the beginning of the 
# dictionary, and the ceiling is the first item we added after.

def find_rotation_point(list):
  # Store the first word
  first_word = list[0]

  # Set up ceiling and floor indexes for binary search
  floor_index = 0
  ceiling_index = len(list) - 1

  while floor_index < ceiling_index:
    # Guess a halfway point between floor and ceiling index
    guess_index = floor_index + ((ceiling_index - floor_index) / 2)

    # if guess comes after first word or is the first word...
    if list[guess_index] >= first_word:
      # Go right
      floor_index = guess_index

    # else go left
    else:
      ceiling_index = guess_index

    # If we floor and ceiling have converged
    if floor_index + 1 == ceiling_index:
      # Ceiling and floor have converged next to each other
      # But our list still remains sorted, so the list was never rotated
      if list[ceiling_index] >= list[floor_index]:
        return 0
      # between floor and ceiling is where we flipped to the beginning
      # so ceiling is alphabetically first
      return ceiling_index

print find_rotation_point(['z','a','b','c','d','e','g'])
# print find_rotation_point(
#   [ 'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage'])
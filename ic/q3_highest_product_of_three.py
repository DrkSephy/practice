# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.


from itertools import islice

# Approach 1: Greedy method to solve in O(n) time
def highest_product(list_of_ints):
  # Start at 3rd item (index 2)
  # Pre-populate highests and lowests based on the first two items
  # Could have initialized the values to be None, but this is cleaner
  highest = max(list_of_ints[0], list_of_ints[1])
  lowest  = min(list_of_ints[0], list_of_ints[1])

  highest_product_of_two = list_of_ints[0] * list_of_ints[1]
  lowest_product_of_two  = list_of_ints[0] * list_of_ints[1]

  # Pre-populate highest_product_of_three with the first three items
  highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

  # Walk through list from index 2
  for current in islice(list_of_ints, 2, None):
    # Check for new highest product of three
    highest_product_of_three = max(current * highest_product_of_two, current * lowest_product_of_two, highest_product_of_three)

    # Check for new highest product of two
    highest_product_of_two = max(current * highest, current * lowest)

    # Check for new lowest product of two
    lowest_product_of_two = min(current * highest, current * lowest)

    # Check for new highest value
    highest = max(highest, current)

    # Check for new lowest value
    lowest = min(lowest, current)

  return highest_product_of_three

print highest_product([1, -2, 3, 4, -5, -2])


# Find all permutations of a string.

def find_permutations(str):
  # base case
  if len(str) <= 1:
    return set([str])

  all_chars_except_last = str[:-1]
  last_char = str[-1]

  # recursive call: get all possible permutations for all chars except last
  permutations_of_all_chars_except_last = find_permutations(all_chars_except_last)
  print permutations_of_all_chars_except_last

  # put the last char in all possible positions for each of the above permutations
  permutations = set()

  # For each permutation...
  for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
    for position in range(len(all_chars_except_last) + 1):
      permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
      permutations.add(permutation)
  return permutations

print find_permutations('cat')

def total_subsets_matching_sum(numbers, sum):
  array = [1] + [0] * (sum)
  for current_number in numbers:
    for num in xrange(sum - current_number, -1, -1):
      if array[num]:
        array[num + current_number] += array[num]
  return array[sum]


print total_subsets_matching_sum(range(1, 10), 9) 
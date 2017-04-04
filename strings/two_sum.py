# Given an unsorted array, find the two indicies that sum to a specific value.

# Complexity: O(n) time, O(n) space

def two_sum(nums, target):
  if nums is None or target is None:
      raise TypeError('nums or target cannot be None')
  if not nums:
      raise ValueError('nums cannot be empty')
  cache = {}
  for index, num in enumerate(nums):
      cache_target = target - num
      if num in cache:
          return [cache[num], index]
      else:
          cache[cache_target] = index
  return None

print two_sum([1, 3, 2, -7, 5], 7)

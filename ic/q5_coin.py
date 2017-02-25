# Write a function that given:
#   1. an amount of money
#   2. a list of coin denominations
# computes the number of ways to make amount of money with coins of the available denominations.

# Approach #1: Recursion + memoization
# Runtime: O(n * m) Space: O(n * m)
# Recursive solution (top-down) can generate a large call stack for arbitrary inputs,
# which can cause a stack overflow.
# class Change:
  
#   def __init__(self):
#     self.memo = {}

#   def change_possibilities_topdown(self, amount_left, denominations, current_index=0):
#     # Check our memo and short-circuit if we have already solved this one
#     memo_key = str((amount_left, current_index))
#     if memo_key in self.memo:
#       print "grabbing memo[%s]" % memo_key
#       return self.memo[memo_key]


#     # Base cases
#     # We got the right amount
#     if amount_left == 0: return 1

#     # We overshot the amount (used too many coins)
#     if amount_left < 0: return 0

#     # We used up all denominations
#     if current_index == len(denominations): return 0

#     print "checking ways to make %i with %s" % (amount_left, denominations[current_index:])

#     # Choose a current coin
#     current_coin = denominations[current_index]

#     # See how many possibilities we can get
#     # For each number of times to use current_coin
#     num_possibilities = 0
#     while amount_left >= 0:
#       num_possibilities += self.change_possibilities_topdown(amount_left, denominations, current_index + 1)
#       amount_left -= current_coin

#     # Save the answer in our memo so we don't compute it again
#     self.memo[memo_key] = num_possibilities
#     return num_possibilities

# changer = Change()
# print changer.change_possibilities_topdown(4, [1, 2, 3])

# Approach 2: Bottom-up
# Runtime: O(n * m), Space: O(n)
def change_possibilities_bottom_up(amount, denominations):
  ways_of_doing_n_cents = [0] * (amount + 1)
  ways_of_doing_n_cents[0] = 1

  # For every coin we have
  for coin in denominations:
    for higher_amount in xrange(coin, amount + 1):
      print (higher_amount, coin, amount + 1)
      higher_amount_remainder = higher_amount - coin
      ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
      # print ways_of_doing_n_cents

  return ways_of_doing_n_cents[amount]

print change_possibilities_bottom_up(4, [1, 2, 3])



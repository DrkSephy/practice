# Write an efficient function that takes stock_prices_yesterday and returns 
# the best profit I could have made from 1 purchase and 1 sale of 1 Apple 
# stock yesterday.

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# Brute force approach [O(n^2)]
# def get_max_profit(stock_prices_yesterday):

#     max_profit = 0

#     for outer in xrange(len(stock_prices_yesterday)):
#       for inner in xrange(len(stock_prices_yesterday)):
#         # For each pair of i, j, find the earlier and later times
#         earlier = min(outer, inner)
#         later = max(outer, inner)

#         earlier_price = stock_prices_yesterday[earlier]
#         later_price = stock_prices_yesterday[later]
#         print 'Earlier: ', earlier_price, ' Later: ', later_price

#         # Calculate profit if we bought at the earlier price and sold at the lower price
#         potential_profit = later_price - earlier_price

#         max_profit = max(max_profit, potential_profit)

#     return max_profit

# More efficient brute force approach [O(n^2)]
# def get_max_profit(stock_prices_yesterday):

#   max_profit = 0

#   # go through every price (with its index as the time)
#   for earlier_time, earlier_price in enumerate(stock_prices_yesterday):

#       # and go through all the LATER prices
#       for later_price in stock_prices_yesterday[earlier_time+1:]:

#           # see what our profit would be if we bought at the
#           # earlier price and sold at the later price
#           potential_profit = later_price - earlier_price

#           # update max_profit if we can do better
#           max_profit = max(max_profit, potential_profit)

#   return max_profit

# Approach 3 [O(n)]
# Keep track of the lowest price we've seen so far
# See if we can get a better profit
# def get_max_profit(stock_prices_yesterday):
#   min_price = stock_prices_yesterday[0]
#   max_profit = 0
#   for current_price in stock_prices_yesterday:
#     # Check if min price is the lowest we've seen so far
#     min_price = min(min_price, current_price)

#     # Check potential profit
#     potential_profit = current_price - min_price

#     # Update max profit
#     max_profit = max(max_profit, potential_profit)
#   return max_profit

# What about edge cases? What is the stock value stays the same?
#   - If the stock value stays the same, we will return 0. We are covered
# What if it goes down all day?
#   - Return the best we could do while losing money

# Approach 4, handling negative profit [O(n) runtime, O(1) space]
# Using a greedy approach, going through the list only once
# And updating values along the way

def get_max_profit(stock_prices_yesterday):

  # Make sure we have at least 2 prices
  if len(stock_prices_yesterday) < 2:
    raise IndexError('Getting a profit requires at least 2 prices')

  # We'll greedily update min_price and max_profit, so we initialize them
  # to the first price and the first possible profit
  min_price = stock_prices_yesterday[0]
  max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

  for index, current_price in enumerate(stock_prices_yesterday):
    # Skip the 0th index, we can't buy and sell at the same time stamp
    if index == 0:
      continue

    # See what our profit would be if we bought at the min price and sold at the current price
    potential_profit = current_price - min_price

    # Update max profit if we can do better
    max_profit = max(max_profit, potential_profit)

    # Update the min price so its always the lowest one we've seen so far
    min_price = min(min_price, current_price)
  return max_profit

print get_max_profit(stock_prices_yesterday)


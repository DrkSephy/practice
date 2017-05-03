# Given stock prices in an array, print the maximum
# profit from a buy and sell.

# i.e, [19, 22, 15, 35, 40, 10, 20] -> Profit of 25.

# Solve it in O(N) time.

def stock_gain(prices):
  # Pick first element as arbitrary min
  min_price = prices[0]


  # Choose arbitrary max profit
  max_profit = prices[1] - prices[0]

  # Loop over prices
  for index, val in enumerate(prices):
    # Skip index 0, we can't buy + sell at the same time
    if index == 0:
      pass


    # Compute new profit
    potential_profit = val - min_price

    max_profit = max(potential_profit, max_profit)

    # Compute new min
    min_price = min(min_price, val)
  return max_profit

print stock_gain([19, 22, 15, 35, 40, 10, 20, 100])
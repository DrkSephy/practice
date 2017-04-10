# Count the number of ways to make change given n coins.

# Complexity: O(mn), n operations on m coins each
# Space: O(n)

def change(n, coins):
  arr = [1] + [0] * n
  for coin in coins:
    for i in range(coin, n + 1):
      arr[i] += arr[i - coin]
  print arr
  return 0 if n == 0 else arr[n]
  # print arr

print change(5, [1, 2, 3])
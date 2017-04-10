def knapsack(val, weight, w):
  k = [[0 for x in range(len(val) - 1)] for j in range(w + 1)]
  for i in range(0, len(val)):
    for j in range(w):
      print j
      # print k[i][j]


val = [22, 20, 15, 30, 24, 54, 21, 32, 18, 25]
weight = [4, 2, 3, 5, 5, 6, 9, 7, 8, 10]
knapsack(val, weight, 30)
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

# sort numbers in place
a.sort()

# check all adjacent pairs
min_diff = float('inf')
for i in xrange(n - 1):
    if abs(a[i] - a[i+1]) < min_diff:
        min_diff = abs(a[i] - a[i+1])
print min_diff
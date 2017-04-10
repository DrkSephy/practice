# https://www.hackerrank.com/challenges/the-birthday-bar

import sys

def getWays(squares, d, m):
    # Complete this function
    num_ways = 0
    for index, value in enumerate(squares):
        # iterate over number of nums
        result = sum(squares[index:index + m])
        if result == d:
            num_ways += 1
    return num_ways
            

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

import sys

def getRecord(s):
    # Complete this function
    best = 0
    worst = 0
    best_score = s[0]
    worst_score = s[0]
    for score in s:
        # Check if we hit a new max
        if score > best_score:
            # set new max
            best_score = score
            best += 1
        # Check if we hit a new low
        if score < worst_score:
            worst_score = score
            worst += 1
    return [best, worst]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
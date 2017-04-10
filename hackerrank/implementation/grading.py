# https://www.hackerrank.com/challenges/grading

#!/bin/python

import sys
import math

def solve(grades):
    # Complete this function
    for grade in grades:
        # round to nearest upwards multiple of 5
        rounded = int(math.ceil(grade/5.0)) * 5.0
        diff = abs(rounded - grade)
        if diff < 3:
            if rounded < 40:
                print int(grade)
            else:
                print int(rounded)
        else:
            print int(grade)

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
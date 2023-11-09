#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    ways = [0] * (n+1)
    ways[0] = 1
    
    for i in range(len(c)): # 0 1
        for j in range(c[i], n+1): # 3 2
            ways[j] += ways[j-c[i]] # 1 0 1 1 1
        print(c[i], ways)
            
    return ways[n]
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(ways)
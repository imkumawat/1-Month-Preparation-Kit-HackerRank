#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0
    larr = sorted(arr)
    for i in range(4):
        min = min + larr[i]
    barr = sorted(arr)
    for i in range(1, 5):
        max = max + barr[i]

    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

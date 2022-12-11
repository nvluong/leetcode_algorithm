#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)
    if n == d:
        return arr
    else:
        d = d % n
        print(d)
        a = arr[:d]
        b = arr[d:]
        print("a ", a)
        print("b ", b)

        for i in range(len(b)):
            arr[i] = b[i]
        print(arr)
        for i in reversed(range(len(a))):
            print("i ", i)
            print("i - d ", i-d)
            arr[i-d] = a[i]
        print(arr)
        return arr
d = 1
arr = [1,2,3,4,5]
print(rotateLeft(d, arr))

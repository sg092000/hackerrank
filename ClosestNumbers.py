#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    ans = 9999999
    lst = []
    for i in range(len(arr)-1):
        ans = min(ans , arr[i+1] - arr[i])
    
    for i in range(len(arr)-1):
        if(ans == arr[i+1]-arr[i]):
            lst.append(arr[i])
            lst.append(arr[i+1])
            
    return lst

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

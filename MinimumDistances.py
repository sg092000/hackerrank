#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    dict = {}
    for i in range(len(a)):
        n = a[i]
        if n in dict:
            dict[n].append(i)
        else:
            dict[n] = []
            dict[n].append(i)
    ans = 999999
    for x in dict:
        for i in range(len(dict[x])-1):
           ans = min(ans,dict[x][i+1] - dict[x][i]) 
    if(ans == 999999):
        ans = -1
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

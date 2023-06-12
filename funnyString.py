#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def funnyString(s):
    # Write your code here
    srev = s[::-1]
    sascii = []
    result = []
    for i in s:
        sascii.append(ord(i))
    print("sAscii", sascii)
    for i in range(len(sascii)-1):
        res = abs(sascii[i+1] - sascii[i])
        result.append(res)
    print("SResult", result)
    srevascii = sascii
    srevascii.reverse()
    print("Srevascii", srevascii)
    revresult = []
    for i in range(len(srevascii)-1):
        res = abs(srevascii[i+1] - srevascii[i])
        revresult.append(res)
    print("Srevresult", revresult)
    if result == revresult:
        return 'Funny'
    else:
        return 'Not Funny'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()










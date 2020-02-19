#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

# Complete the reverseArray function below.
def standardDev(count, elements):

    mean = statistics.mean(elements)

    sDev = statistics.pstdev(elements, mean)
    
    fptr.write(str(round(sDev,1)))
    fptr.write('\n')
    return 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr_ele = list(map(int, input().rstrip().split()))

    standardDev(arr_count, arr_ele)



    fptr.close()

#5
#10 40 30 50 20

# Output 14.1
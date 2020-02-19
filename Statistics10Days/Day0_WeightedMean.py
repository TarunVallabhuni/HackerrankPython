#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the reverseArray function below.
def weightedMean(elements, wgts):

    s = 0
    for element, wgt in zip(elements, wgts):
        s += element * wgt

    average = s / sum(wgts)
    
    fptr.write(str(round(average,1)))
    fptr.write('\n')
    return 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr_ele = list(map(int, input().rstrip().split()))
    arr_weights = list(map(int, input().rstrip().split()))

    weightedMean(arr_ele, arr_weights)



    fptr.close()

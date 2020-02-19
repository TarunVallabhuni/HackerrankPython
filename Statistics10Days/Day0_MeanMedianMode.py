#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
import pandas as pd 

# Complete the reverseArray function below.
def summaryStatistics(a):
    mean = statistics.mean(a)
    median = statistics.median(a)
    df = pd.DataFrame(a)
    mode = df.mode()[0][0]

    fptr.write( str(mean)+'\n')
    fptr.write( str(median)+'\n')
    fptr.write( str(mode)+'\n')
    fptr.write('\n')
    return 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    summaryStatistics(arr)



    fptr.close()

# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

# Output 
# 43900.6
# 44627.5
# 4978
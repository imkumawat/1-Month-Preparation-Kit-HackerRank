#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    data = s.split(":")

    if str(data[2])[2:] == 'PM':

        if (int(data[0]) == 12):
            sec = str(data[2])[:2]
            data[2] = sec
            return (':').join(data)

        else:
            hr = int(data[0]) + 12
            data[0] = str(hr)
            sec = str(data[2])[:2]
            data[2] = sec
            return (':').join(data)
    else:
        if (int(data[0]) == 12):
            sec = str(data[2])[:2]
            data[2] = sec
            data[0] = str('00')
            return (':').join(data)

        else:

            sec = str(data[2])[:2]
            data[2] = sec
            return (':').join(data)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

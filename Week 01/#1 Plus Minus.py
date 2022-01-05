from decimal import *


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p = 0
    m = 0
    z = 0
    l = len(arr)
    for i in arr:
        if i < 0:
            m = m + 1
        elif i > 0:
            p = p + 1
        else:
            z = z + 1

    print(round(Decimal(p / l), 6))
    print(round(Decimal(m / l), 6))
    print(round(Decimal(z / l), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

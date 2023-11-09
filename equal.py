#!/bin/python3
#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    opperations = 0
    
    while min(arr) != max(arr):
        diff = max(arr) - min(arr)
        
        for i in range(len(arr)):
            if arr[i] != max(arr):
                arr[i] += diff
                
        opperations += 1

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        print(result)

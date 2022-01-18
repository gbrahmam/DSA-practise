import math

def fund(arr, n):
    total = 0
    for i in range(n):
        total += math.ceil(0.07*arr[i])
    return total

n = int(input())
arr = [int(x) for x in input().split()]

print(fund(arr, n))
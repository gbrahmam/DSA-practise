# 1. Given a sorted array of distinct integers, find if there is a pair with a given sum.


def findPairWithSum(arr, x):
    i = 0
    j = len(arr) - 1

    while j > i:
        if arr[i] + arr[j] == x:
            return True
        elif arr[i] + arr[j] > x:
            j -= 1 # j = j - 1
        else: # arr[i] + arr[j] < x:
            i += 1

    return False


arr = [1, 2, 5, 6, 8, 10, 12, 13, 14, 18, 20, 21, 25, 30]

x = 54

print(findPairWithSum(arr, x))




























# 2. Move all zeroes to end of an integer array, order of all other elements should be same.
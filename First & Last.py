def findFirstOccurence(arr, target):
    left = 0
    right = len(arr) - 1

    result = -1

    while left <= right:
        mid = (left + right) // 2
        potentialMatch = arr[mid]

        if target == potentialMatch:
            result = mid
            right = mid - 1
        elif target > potentialMatch:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def findLastOccurence(arr, target):
    left = 0
    right = len(arr) - 1

    result = -1

    while left <= right:
        mid = (left + right) // 2
        potentialMatch = arr[mid]

        if target == potentialMatch:
            result = mid
            left = mid + 1
        elif target > potentialMatch:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


n = int(input())
nums = [int(x) for x in input().split()]
key = int(input())
print(findFirstOccurence(nums,key), findLastOccurence(nums,key))

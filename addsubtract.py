def addsub(target,Arr,n):
#base cases either i reach the target sum or move out of range
    if target == 0 and n==0:
        return 1
    if n<0:
        return 0
#possibility1
    a = addsub(target,Arr,n-1)
#i choose and do either + or -
    b = addsub(target-Arr[n],Arr,n-1) + addsub(target+Arr[n],Arr,n-1)
    return a+b

target = int(input())
n = int(input())
Arr = [int(x) for x in input().split()]
print(addsub(target,Arr,n-1))



                                                                             #Approach2

def findTotalWays(arr, i, k):

    if (k == 0 and i == len(arr)): # If target is reached
        return 1   
 
    # If all elements are processed and target is not reached
    if (i >= len(arr)):
        return 0
 
    # Return total count of three cases
    # 1. Don't consider current element
    # 2. Consider current element and
    # subtract it from target
    # 3. Consider current element and
    # add it to target
    return (findTotalWays(arr, i + 1, k) + findTotalWays(arr, i + 1, k - arr[i]) + findTotalWays(arr, i + 1, k + arr[i]))

target = int(input())
n = int(input())
Arr = [int(x) for x in input().split()]
print(findTotalWays(Arr,0,target))

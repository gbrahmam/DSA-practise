def firstoccurance(arr,start):
    l = 0
    r = len(arr)-1
    res = -1
    while l<=r:
        mid = (l+r)//2
        
        if start==arr[mid]:
            res = mid
            r = mid-1
        elif start>arr[mid]:
            l = mid+1
        else:
            res = mid
            r = mid-1
    
    return res

def lastoccurance(arr,end):
    l = 0
    r = len(arr)-1
    res = -1
    while l<=r:
        mid = (l+r)//2
        
        if end==arr[mid]:
            res=mid
            l = mid+1
        elif end>arr[mid]:
            res = mid
            l = mid+1
        else:
            r = mid-1
    
    return res

tot_ele = int(input())
elements = [int(x) for x in input().split()]
Range=[int(i) for i in input().split()]
res1 = firstoccurance(elements,Range[0])
res2 = lastoccurance(elements,Range[1])
# print(res1, res2)
if res1<=res2:
    print(res1, res2)
else:
    print(-1, -1)
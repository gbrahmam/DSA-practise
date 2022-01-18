# your code goes here
def find_k(l, k):
    # Implement this and return YES if found else return No
    if k<=l[0]:
        return 0
    if k>l[-1]:
        return len(l)-1
    left=0
    right = len(l)-1
    res=-1
    while left<=right:

        mid = (left+right)//2
        pos_match = l[mid]

        if pos_match==k:
            return mid
        elif k<pos_match:
            right = mid-1
            if k-l[mid-1]>=l[mid]-k:
                res=mid
            else:
                res = mid-1
        elif k>pos_match:
            left = mid+1
    return res
N,Q = [int(i) for i in input().split()]
nums = [int(x) for x in input().split()]
queries = [int(idx) for idx in input().split()]
for each in queries:
    print(nums[find_k(nums,each)])
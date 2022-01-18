def find_k(l, k):
    # Implement this and return YES if found else return No
    if k<=l[0]:
        return 0
    if k>l[-1]:
        return len(l)
    left=0
    right = len(l)-1
    res=-1
    while left<=right:

        mid = (left+right)//2
        pos_match = l[mid]

        if pos_match==k:
            return mid
        elif k<pos_match:
            res = mid
            right = mid-1
        elif k>pos_match:
            left = mid+1
    return res

testcases = int(input())
for _ in range(testcases):
    nums = [int(x) for x in input().split()]
    tot_inserts = int(input())
    queries = [int(idx) for idx in input().split()]
    for i in range(tot_inserts):
        print(find_k(nums,queries[i]))
def find_k(l, k):
    # Implement this and return YES if found else return No
    left=0
    right = len(l)-1

    while left<=right:

        mid = (left+right)//2
        pos_match = l[mid]

        if pos_match==k:
            return 'YES'
        elif k<pos_match:
            right = mid-1
        elif k>pos_match:
            left = mid+1
    
    return 'NO'
    
from sys import stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))
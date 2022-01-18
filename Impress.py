from sys import stdin,stdout
def Which_Day(a, x):
    # Implement This
    if x<a[0]:
        return 0
    l = 0
    r = len(a)-1
    res=-1
    while l<=r:
        mid = (l+r)//2
        
        if x==a[mid]:
            return mid
        elif x<a[mid]:
            res=mid
            r=mid-1
        else:
            l=mid+1
    return res        
    
n,q = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
for i in range(n):
    if i!=0:
        a[i] = a[i-1]+a[i]
k = list(map(int,stdin.readline().split()))
for i in range(q):
    ans = Which_Day(a,k[i])+1
    stdout.write(str(ans)+"\n")
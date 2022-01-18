def Where_to_place(l, x):
   # Implement This
    left = 0
    right = len(l)-1

    while left<=right:
        mid = (left+right)//2
        pos_match = l[mid]
       
        if x>pos_match:
           left=mid+1
        
        elif x<=pos_match:
            right = mid -1
    return left
n=int(input())
l=list(map(int,input().split()))[:n]
sum=0
l.sort()
for i in range(n):
    sum+=l[i]
    avg=sum//(i+1)
    l[i]=avg
# print(l)  
t=int(input())    
for k in range(t):
    x=int(input())
    print(Where_to_place(l,x))
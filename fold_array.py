n = int(input())                                   # takes input
Arr1 = []                                          # stores
for i in range(n):           
    Arr1.append(int(input()))
k = int(input())                                    # times to fold
j=1
m = 2                                                 # keeps count of folds
while j != k:

    if n%2==0:                                      # if given arr is even len 
        mid = n//m
        for i in range(mid):
            Arr1[i] = Arr1[i]+Arr1[n-1-i]
        for k in range(mid,n):
            Arr1[k]=0
        j+=1
        m*=2
    
    elif n%2 !=0:
        mid = n//2
        for i in range(mid):
            Arr1[i] = Arr1[i]+Arr1[n-1-i]
        for k in range(mid+1,n):
            Arr1[k]=0
        j+=1

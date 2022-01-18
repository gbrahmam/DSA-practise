t = int(input())                                 #1 0
for i in range(t):                               #t 1
    n = int(input())                             #1 1
    arr = [int(x) for x in input().split()]      #1  n
    peak = -1                                    #1  1
    if n==1:                                 
        peak = 1
    elif arr[0]>arr[1]:
        peak = 1
    else:                                        #1  0
        for i in range(1,n-1):                   #n-1 1
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:   #n 0
                peak = i+1                           #1 1
                break
        if peak == -1:
            if arr[-1]>arr[-2]:
                peak = n
    print(peak)                                  #1  0

    #time complexity = O(n) ----->2n+5
    #space ccomplexity = O(n)------>5+n
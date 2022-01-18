t = int(input())

for i in range(t):
    
    n = int(input())
    
    Arr = [int(x) for x in input().split()]
    # print(Arr)
    # print()
    d1 = {}
    for i in range(n):
        d1[Arr[i]] = i
    # print(d1)
    # print()
    Arr.sort()
    # print(Arr)
    # print()
    d2={}
    for j in range(n):
        d2[Arr[j]]=j
    # print(d2)
    swaps = 0
    for each in d1:
        if abs(d1[each]-d2[each])%2==1:
            swaps+=1
    
    print(swaps//2)



                                                                            #Approah2

# your code goes here
t = int(input())

for i in range(t):
    
    n = int(input())
    
    Arr = [int(x) for x in input().split()]
    # print(Arr)
    # print()
    d1 = set()
    for i in range(0,n,2):
        d1.add(Arr[i])
    # print(d1)
    # print()
    Arr.sort()
    # print(Arr)
    # print()
    d2 = set()
    for j in range(0,n,2):
        d2.add(Arr[j])
    # print(d2)
    swaps = len(d1.difference(d2))
    # for each in d1:
    #     if abs(d1[each]-d2[each])%2==1:
    #         swaps+=1
    
    print(swaps)
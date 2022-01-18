def recurprint(L,R):
    
    # print(L)
    if L == R:
        Arr.append(R)
        # print(Arr)
        return Arr
    
    Arr.append(L)
    return recurprint(L+1,R)

n = int(input())

for i in range(n):
    Arr = []
    L,R = input().split(' ')
    L,R = int(L),int(R)
    # print(L)
    # print(R)
    
    res = recurprint(L,R)
    
    for each in res:
        print(each,end=' ')
    print()
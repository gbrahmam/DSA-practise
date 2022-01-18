def diagnols_sum(lst,size):
    summ = 0
    if size == 1:
        return (Arr1[0][0]*2)
    for i in range(size):
        summ+=lst[i][i]
    
    for i in range(size):
        summ+=lst[i][size-1-i]
    
    return summ

m = int(input())
Arr1 = []
for i in range(0,m):
    Arr1.append([int(x) for x in input().split(' ')])

res = diagnols_sum(Arr1,m)
print(res)
def sumofproduct(n):
    # Code here
    add = 0 
    y=0
    for i in range(1,n+1):
        prod = 1
        y = n//i
        prod*=(i*y)
        add+=prod
    return add
n = int(input())
print(sumofproduct(n))
def recurmult(n,prod):
    
    if n==0:
        return prod
    
    rem = n%10
    # if rem == 0:
    #     return 0
    prod*=rem
    n = n//10
    return recurmult(n,prod)
    
t = int(input())

for i in range(t):
    prod = 1
    n = int(input())
    if n == 0:
        print(n)
    elif n<0:    
        n = abs(n)
        print(recurmult(n,prod))
    else:
        print(recurmult(n,prod))
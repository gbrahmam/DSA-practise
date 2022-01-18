def series9(n):
    summ = 0
    if n == 0:
        return 0
    
    if n>0:
        # k = n+1
        for i in range(n+1):
            summ+= (10**i)-1
            
        return summ
    

n = int(input())

print(series9(n))
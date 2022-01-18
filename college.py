def sumofdivisors(n):
    summ = 0
    for i in range(1,n+1):
        if n%i==0:
            summ+=i
    return(summ)

n = int(input())
print(sumofdivisors(n))
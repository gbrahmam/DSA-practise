def factorial(n):
    
    if n<0:
        return ('undefined')
    
    if n == 0:
        return 1
        
    if n>0:
        return n*factorial(n-1)


n = int(input())

res = factorial(n)

print(res)
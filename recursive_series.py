def recurseries(n):
    
    if n<=9:
        return n
    
    if n%2 !=0:
        return recurseries(n-9)
    
    else:
        return recurseries(n-10)

    
for i in range(int(input())):
    
    n = int(input())
    print(recurseries(n))
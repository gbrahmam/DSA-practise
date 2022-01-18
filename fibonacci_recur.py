def fibonacci(n):
    
    if n == 1:
        print(n,'@')
        return 0
    
    if n == 2:
        print(n,'$')
        return 1
        
    if n>2:
        print(n,'#')
        return fibonacci(n-1)+fibonacci(n-2)
        
        
for i in range(int(input())):
    
    n = int(input())
    print(fibonacci(n))
def distcover(n):
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
        
    if n == 2:
        return 2
        
    if n>2:
        return distcover(n-1) + distcover(n-2)

for i in range(int(input())):
    
    n = int(input())
    print(distcover(n))
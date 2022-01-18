def reqseq(n):
    
    if n == 1:
        return 1
    
    else:
        res = 0
        j = 1
        for i in range(1,n+1):
        
            prod = 1
        
            while i>0:
                prod*=j
                i-=1
                j+=1
        
            res+= prod
            
        return res
    
t = int(input())

for i in range(t):    
    n = int(input())
    print(reqseq(n))
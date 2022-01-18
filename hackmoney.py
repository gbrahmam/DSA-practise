def hackmoney(n):
    
    if n==0:
        return False
    
    if n == 1:
        # print(n,'1')
        return True
    
    if n > 1:
        
        if n%20 == 0 and n%10 == 0:
            # print(n,'3')
            return hackmoney(n//20) or hackmoney(n//10)   # return boolean to compare
        
        elif n%10 == 0:
            # print(n,'4')
            return hackmoney(n//10)

        return False

t = int(input())

for i in range(t):
    
    n = int(input())
    if (hackmoney(n)) == True:
        print('Yes')
    else:
        print('No')
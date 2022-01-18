n = int(input())            
        
Arr1 = []               
x = 1                    
y = 1                   
for i in range(n):      
    val = int(input())  
    y = x               
    x = val             
    prod = x * y        
    Arr1.append(prod)   
    # print(Arr1)
print(max(Arr1))        
    
    # Tc = 6+6n---->O(n)      S = 6+n----->O(n)
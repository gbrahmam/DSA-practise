n = int(input())           #1  1
Arr1 = []                  #1  0
for i in range(n):         #n  1
    val = int(input())     #n  1    
    Arr1.append(val)       #n  n
Arr2 = []                  #1  0
for i in range(1,n):       #n-1 1
    val=Arr1[i]*Arr1[i-1]  #n-1 1
    Arr2.append(val)       #n-1 1
max_prod = max(Arr2)       #1   1
print(max_prod)            #1  0

# Tc = 6n+2----> O(n)      S = n+7----> O(n)
n = int(input())
Arr = [int(i) for i in input().split(' ')]

for i in range(1,n):
    key_ele = Arr[i]
    
    while i>0:
        
        if key_ele>=Arr[i-1]:
            break
        else:
            Arr[i-1],Arr[i] = Arr[i],Arr[i-1]
            key_ele = Arr[i-1]
            i-=1

curr_min = float('inf')

for i in range(n):
    
    for j in range(i+1,n):
        
        diff = Arr[j] - Arr[i]
        curr_min = min(diff,curr_min)

print(curr_min)
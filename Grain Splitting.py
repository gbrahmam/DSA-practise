# your code goes here
t = int(input())
print(t)
for i in range(t):
    
    Arr = [int(x) for x in input().split()]
    left_sum = 0
    right_sum = sum(Arr)
    Arr.sort()
    i = 0
    while left_sum!=right_sum:
        left_sum+=Arr[i]
        right_sum-=Arr[i]
        i+=1
    if (i+1)>(len(Arr)//2):
        print(*Arr[i:len(Arr)])
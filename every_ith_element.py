n = int(input())          # 1  1
Arr = []                  # 1  0
for i in range(n):        # n  1
    val = int(input())    # n  1
    Arr.append(val)       # n  n
i = int(input())          # 1  1
summ = 0                  # 1  1
for j in range(i-1,n,i):  # n  1   worst case scenario
    summ+=Arr[j]          # n  0
print(summ)               # 1  0

# T = 5n+5---->O(n)    # S = n+6------> O(n)

                               #using while loop

n = int(input())
sum = 0
arr = []
for i in range(n):
    arr.append(int(input()))
x = int(input())
i = x-1
while(i<n):
    sum+=arr[i]
    i+=x
print(sum)
# auxiliary space means extra space---> which we havve to use it definitly, like taking inputs,....
# your code goes here
n = int(input())

Arr = [int(x) for x in input().split()[0:2*n]]

Arr.sort()
# print(Arr)
res=0
for i in range(1,2*n,2):
    res+=min(Arr[i-1],Arr[i])
    # print(res)
print(res)
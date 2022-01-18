n = int(input())
Arr1 = [int(x) for x in input().split()[0:n]]
Arr1.sort()
store =[]
for i in range(1,n):
    val = Arr1[i]-Arr1[i-1]
    store.append(abs(val))
print(min(store))
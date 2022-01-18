n,x = input().split(' ')
n,x = int(n),int(x)

Arr = [int(x) for x in input().split()]
i = len(Arr)

Arr.append(x)
# print(Arr)
# print('============')
key_ele = x

while i>0 and key_ele<Arr[i-1]:
    Arr[i] = Arr[i-1]
    i-=1
Arr[i] = key_ele

for each in Arr:
    print(each,end=' ')
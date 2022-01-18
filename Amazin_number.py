# your code goes here
elements = int(input())
Arr = []
for idx in range(elements):
    Arr.append(int(input()))
flag = False
for idx in range(1,elements):
    if Arr[idx]+Arr[idx-1]>100:
        flag =True
        break
print(flag)
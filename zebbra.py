n = int(input())
Arr =[]
for i in range(n):
    val = int(input())
    if val>0:
        Arr.append(1)
    else:
        Arr.append(0)
# print(Arr)
for i in range(1,n):
    flag = True
    if Arr[i]==Arr[i-1]:
        flag = False
        print(flag)
        break
if flag == True:
    print(flag)
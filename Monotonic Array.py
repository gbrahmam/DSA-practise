n = int(input())
Arr = []
flag = True
for i in range(n):
    Arr.append(int(input()))

for i in range(1,n):
    if Arr[i]==Arr[i-1]:
        continue
    else:
        store = i
        break

if i!=n-1:
    j = store
    
    if Arr[j]>Arr[j-1]:                #increasing cond
        store+=1
        for i in range(store,n):
            if Arr[i]>=Arr[i-1]:
                continue
            else:
                flag = False
                break


    elif Arr[j]<Arr[j-1]:              #decreasing cond
        store+=1
        for i in range(store,n):
            if Arr[i]<=Arr[i-1]:
                continue
            else:
                flag = False
                break

print(flag)
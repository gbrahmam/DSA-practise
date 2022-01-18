n =int(input())
Arr =[]
for i in range(n):
    Arr.append(int(input()))
count = 1
max_count = 4
for i in range(1,n):
    if Arr[i]==Arr[i-1]:
        count+=1
        if count==max_count:
            print(Arr[i])
            break
    else:
        count=1
if count==1:
    print(-1)
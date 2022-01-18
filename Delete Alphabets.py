row,column = [int(x) for x in input().split()]
Arr =[]
for i in range(row):
    Arr.append(input())
count = 0
for i in range(column):
    for j in range(1,row):
        if Arr[j][i]<Arr[j-1][i]:
            count+=1
            break
print(count)
n = int(input())

num_Arr = []
for i in range(n):
    num_Arr.append(int(input()))


index_Arr = []
for i in range(n):
    index_Arr.append(int(input()))


target_Arr = []

for i in range(n):
    target_Arr.insert(index_Arr[i],num_Arr[i])
    
for each in target_Arr:
    print(each)
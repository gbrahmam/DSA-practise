# your code goes here
from collections import Counter
arr_len = int(input())
arr =[]
for i in range(arr_len):
    arr.append(int(input()))
# print(arr)
freq = Counter(arr)
# print(freq)
d = sorted(freq.items())
# print(d)
d_count={}
temp =0
for i in range(len(d)):
    d_count[d[i][0]]=temp
    temp+=d[i][1]

res = []
for each in arr:
    res.append(d_count[each])

for each in res:
    print(each)
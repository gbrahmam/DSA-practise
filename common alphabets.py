from collections import Counter
Arr = []
n=int(input())
for i in range(n):
    Arr.append(input())

d ={}
for each in Arr[0]:
    if each not in d:
        d[each]=1
    else:
        d[each]+=1

for word in Arr[1:n]:
    d1 = Counter(word)
    
    for each in d:
        d[each]=min(d[each],d1[each])
# print(d)
for i,v in sorted(d.items()):
    if d[i]!=0:
        print(i, v)
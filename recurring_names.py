k = int(input())
Arr = [x for x in input().split()]
d = {}
for each in Arr:
    if each not in d:
        d[each]=1
    else:
        d[each]+=1
Arr2=[]
for each in sorted(d.keys()):
    if d[each]>k:
       Arr2.append(each)
if len(Arr2)==0:
    print('no such names in this town!!!')
else:
    for each in Arr2:
        print(each)
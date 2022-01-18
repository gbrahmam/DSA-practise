N = int(input())
d = {}
for i in range(N):
    inpstr = input().split()
    d[inpstr[0]] = inpstr[1]
# print(d)

d2 = {}
for each in d.values():
    if each not in d2:
        d2[each] = 1
    else:
        d2[each]+=1
# print(d2)

sport_liked = max(d2.values())
for each in sorted(d2.keys()):
    if d2[each]==sport_liked:
        print(each)
        break
if 'football' in d2.keys():
    print(d2['football'])
else:
    print(0)
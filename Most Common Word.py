from collections import defaultdict
import string
paragraph = "a."
exclude = set(string.punctuation)
res = ''.join(ch for ch in paragraph if ch not in exclude)
# print(res)
Arr = [x.lower() for x in res.split()]
d = defaultdict(int)
banned = []
for word in Arr:
    if word not in banned:
        d[word]+=1
# print(d)
count = 0
uniq=''
for each in d:
    if d[each]>count:
        count = d[each]
        uniq = each
print(uniq)
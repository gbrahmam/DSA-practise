from collections import defaultdict
from collections import Counter

d = defaultdict(int)

n = int(input())

Arr = [int(x) for x in input().split()[0:n]]
Arr1 = []

for i in range(n):
    m = 1
    count = 0
    while m<=(Arr[i]//2):
        if Arr[i]%m == 0:
            count+=1
        m+=1
    Arr1.append(count)
# print(Arr1)

d = Counter(Arr1)
# print(d)
pair=0
for i in range(1,n):
    if Arr1[i]!=Arr1[i-1]:
        val = d[Arr1[i-1]]
        if val>=2:
            pair+=(val*(val-1)//2)
if i == n-1:
    val = d[Arr1[i]]
    if val>=2:
        pair+=(val*(val-1)//2)

print(pair)



                                                              #Approach2

from collections import defaultdict
import math

def factor(n):
    count = 0
    for i in range(1,1+int(math.sqrt(n))):
        if n%i == 0:
            count+=1
            if n//i!=i:
                count+=1
    return count
            
d = defaultdict(int)
n = int(input())
Arr = [int(x) for x in input().split()]
Arr1 = []
for each in Arr:
    count = factor(each)
    Arr1.append(count)
# print(Arr1)

for each in Arr1:
    d[each]+=1
# print(d)

pair=0
for each in d:
    pair+=(d[each]*(d[each]-1))//2
print(pair)
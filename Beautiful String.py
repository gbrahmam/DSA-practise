# your code goes here
from collections import defaultdict

def beauty(s):
    d = defaultdict(int)
    d[(0,0)]=1
    count_a = 0
    count_b = 0
    count_c = 0
    res=0
    for char in s:
        if char == 'a':
            count_a+=1
        elif char=='b':
            count_b+=1
        elif char=='c':
            count_c+=1

        key = (count_a - count_b,count_b - count_c)

        res+=d[key]
        d[key]+=1
        
    return res

t = int(input())
for i in range(t):
    svar = input()
    print(beauty(svar))
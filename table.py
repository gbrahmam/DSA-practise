def table(n,m=1):
    if n<=0:
        Arr.append(0)
        return Arr
    if m==10:
        Arr.append(n*10)
        return Arr
    
    Arr.append(n*m)
    return table(n,m=m+1)
        
n = int(input())
m = 10
Arr = []
res = table(n)
if len(res) == 1:
    print(res[0])
else:
    for each in res:
        print(each,end=' ')
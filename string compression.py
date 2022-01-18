def compress(st):
    res=''
    Arr = list(st)
    count = 1
    i =1
    while i<len(Arr):
        if Arr[i]==Arr[i-1]:
            count+=1
        else:
            res+=Arr[i-1]
            if count>1:
                res+=str(count)
            count=1
        i+=1    
    if i==len(Arr):
        res+=Arr[i-1]
        if count>1:
            res+=str(count)
    
    print(res)

t = int(input())
for _ in range(t):
    st = input()
    compress(st)
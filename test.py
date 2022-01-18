                                                                    #60% faster

def rotarr(Arr,m):
    if len(Arr)==1:
        return Arr
    if m>len(Arr):
        m = m%len(Arr)
    temp =[]
    for idx in range(m):
        temp.append(Arr[idx])
    
    i = 0
    j = 0
    while i<(len(Arr) - m):
        Arr[i] = Arr[m+i]
        i+=1
    
    while i<=len(Arr) and j<m:
        Arr[i] = temp[j]
        i+=1
        j+=1
    
    return Arr

n,query = [int(x) for x in input().split()]
Arr= [int(x) for x in input().split()]
for each in range(query):
    pos,val = input().split()
    val=int(val)
    if pos=='L':
        rot_Arr = rotarr(Arr,val)
    elif pos=='R':
        # temp== n - val
        rot_Arr = rotarr(Arr,n-val)
    # print(Arr)
for each in rot_Arr:
    print(each,end=' ')



                                                                           #80% faster
def rotarr(Arr,pos,val):
    if len(Arr)==1 or val==0:
        return Arr
    # arr = []
    val = val%len(Arr)
    if pos=='R':
        val = len(Arr)-val
        # print(val)
    Arr[:] = Arr[val:len(Arr)] + Arr[0:val]
    return Arr

n,query = [int(x) for x in input().split()]
Arr= [int(x) for x in input().split()]
for each in range(query):
    pos,val = input().split()
    res=rotarr(Arr,pos,int(val))
    # print(Arr)
for each in res:
    print(each,end=' ')
def rotarr(Arr,m):
    n = len(Arr1)
    if n == 1:
        return Arr1

    rot = m%n
        
    i = 0
    j = rot-1
    while j >i:
        Arr1[i],Arr1[j] = Arr1[j],Arr1[i]
        i+=1
        j-=1
    
    i = rot
    j = n-1
    
    while j > i:
        Arr1[i],Arr1[j] = Arr1[j],Arr1[i]
        i+=1
        j-=1
    
    i = 0
    j = n-1
    
    while j > i:
        Arr1[i],Arr1[j] = Arr1[j],Arr1[i]
        i+=1
        j-=1
    
    return Arr1

Arr1 = [int(x) for x in input().split(' ')]
m = int(input())
rot_Arr = rotarr(Arr1,m)
for each in rot_Arr:
    print(each)



#                                            2 def metods


# your code goes here
def rotarr(Arr,m):
    n = len(Arr1)
    if n == 1:
        return Arr1

    rot = m%n
    
    revArr(Arr,0,rot-1)
    
    revArr(Arr,rot,n-1)
    
    revArr(Arr,0,n-1)
    
    return Arr
    
    
def revArr(Arr,i,j):
    
    while j>i:
        Arr1[i],Arr1[j] = Arr1[j],Arr1[i]
        i+=1
        j-=1
    
    return Arr

Arr1 = [int(x) for x in input().split(' ')]
m = int(input())
rot_Arr = rotarr(Arr1,m)
for each in rot_Arr:
    print(each)
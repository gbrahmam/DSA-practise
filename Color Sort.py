n = int(input())
Arr = []
for i in range(n):
    Arr.append(int(input()))
if n == 1:
    print(Arr[0])
elif n>1:
    i = 0
    j = 0
  #RED balloon check
    while j<n:                             
        if Arr[j]==0:
            Arr[i],Arr[j] = Arr[j],Arr[i]
            i+=1
        j+=1
    
    j = i
    
    #WHITE Balloon Check
    
    while j<n:
        if Arr[j] == 1:
            Arr[i],Arr[j] = Arr[j],Arr[i]
            i+=1
        j+=1

    for each in Arr:
        print(each)



                                           #  def aapproach


def colorsort(Arr,n):
    i = 0
    j = 0
    if n == 1:
        return(Arr)
 
    else:
        key = [0,1,2]
        for k in range(len(key)-1):
            
            Arr,i,j = sorty(Arr,i,j,key[k])  #for red/WHITE balloons
        
        return Arr

def sorty(Arr,i,j,key):
    
    while j<n:                             
        if Arr[j]==key:
            Arr[i],Arr[j] = Arr[j],Arr[i]
            i+=1
        j+=1
    j = i

    return Arr,i,j

n = int(input())
Arr = []
for i in range(n):
    Arr.append(int(input()))
res = colorsort(Arr,n)
for i in range(len(res)):
    print(res[i])
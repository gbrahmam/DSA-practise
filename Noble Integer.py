n = int(input())               #takes input
Arr1=[]                     #stores input
for i in range(n):
    val = int(input())
    Arr1.append(val)
for i in range(n):
    count = 0                 # this wil count the values greater than P
    flag = True               # tells whether such P exist or not
    for j in range(n):          
        if Arr1[i]<Arr1[j]:    # comparing to find P
            count+=1           # if found counter gets inc
    if count==Arr1[i]:          # for every element we chk the condition for P  
        print(1)                
        flag = False
        break                   #we come out immediately if P found 
if flag == True:                # this will only exec if P not found
    print(-1)



                                             #O(nlogn)


n = int(input())               #takes input
Arr1=[]                     #stores input
for i in range(n):                 #n  1
    val = int(input())             #n  1
    Arr1.append(val)               #n  n
Arr1.sort()                    #nlogn  0
# print(Arr1)
flag = True                        #1 1
for i in range(1,n):               #n  1 
    if Arr1[i-1]==Arr1[i]:         #n  0
        continue                   #n  0   #worst case
    else:
        max_val = n-i              #1  1
        if max_val==Arr1[i-1]:     #1  0
            flag = False           #1  0
            print(1)               #1  0
            break                  #1  0
if flag == True:                   #1  0
    print(-1)                      #1  0

#Tc = 7+6n+nlogn---->  O(nlogn)      S = 5+n------->O(n) 
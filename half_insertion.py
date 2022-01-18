# oldstring = input()
# n = len(oldstring)
# store = 0
# if n%2 == 0:
#     store = n//2
# else:
#     store = n//2 +1
# fhalfstring = oldstring[0:store-1:1]
# shalfstring = oldstring[store-1::1]
# Arr = list(shalfstring)
# for i in range(1,len(shalfstring)):
#     key = Arr[i]
    
#     while i>0 and key<Arr[i-1]:
#         Arr[i]=Arr[i-1]
#         i-=1
    
#     Arr[i] = key
# string = ''
# for each in Arr:
#     string+=each
# print(fhalfstring+string)



oldstring = input()
n = len(oldstring)
store = 0
if n%2 == 0:
    store = n//2
else:
    store = n//2 +1
Arr = list(oldstring)
for i in range(store,n):
    key = Arr[i]
    
    while i>store-1 and key<Arr[i-1]:
        Arr[i]=Arr[i-1]
        i-=1
    Arr[i] = key
for each in Arr:
    print(each,end='')

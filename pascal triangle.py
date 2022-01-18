# n = int(input())                                                           #
# if n >0 and n<3:                                             # for n=1 and 2 it prints 1st 2 rows
#     for i in range(n):
#         print(1)
# elif n>2:
#     Arr1 = [0,1,1,0]                                        #prev row
#     Arr2 = []                                               #current row
#     for i in range(3,n):                                      #for each row
#         Arr2[0]=0                                           #[0......]
#         Arr2[n+1]=0                                         #[0.............0]
#         for i in range(n):                                  #i = [0,1,2,......n-1]
#             Arr2[i+1] = Arr1[i]+Arr1[i+1]                   #[0,1,2,1]
#         Arr1 = Arr2.copy()                                  #Arr2 gets copied to Arr1, storing the prev row to cal the next row
#     print(Arr1)




                                                                #Using Fact  ncr defs

def fact(n):                                  
    if n == 0:                                                #1  0
        return 1                                              #1  0
    else:
        while n>0:                                            #n  0
            return n*fact(n-1)                                #n  0

def NcR(l,m): 
    val = int(fact(l)/((fact(m))*fact(l-m)))                  #1  1
    return val                                                #1  0
    
n = int(input())

if n<3:
    for i in range(n):
        print(1)
else:
    Arr1 = []
    for i in range(n):
        value = NcR(n-1,i)
        Arr1.append(value)
    for i in range(n):
        print(Arr1[i])
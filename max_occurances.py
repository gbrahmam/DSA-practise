n = int(input())                                #1 1
if n:                                           #1 0
    Arr1 =[]                                    #1 0
    for i in range(n):                          #n 1
        Arr1.append(int(input()))               #n n
    max_repval = Arr1[0]                        #1 1
    count=0                                     #1 1
    curr_num = []                               #1 0
    len_coun = []                               #1 0
    for each in Arr1:                           #n 1
        if each == max_repval:                  #n 0
            count+=1                            #n 0
        else:                                   #n 0
            len_coun.append(count)              #n 0
            curr_num.append(max_repval)         #n 0
            max_repval = each                   #n 0
            count=1                             #n 0
    len_coun.append(count)                      #1 0
    curr_num.append(max_repval)                 #1 0
    max_val = max(len_coun)                     #1 1
    for i in range(len(len_coun)):              #n 1
        if len_coun[i]==max_val:                #n 0
            print(curr_num[i])                  #n 0
else:                                          
    print(-1)
    
# T = 10+3n---->O(n)    S = 7+n------>O(n)
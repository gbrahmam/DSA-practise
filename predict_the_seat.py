t = int(input())                                            #1 1
berth = ['L','M','U','L','M','U','SL','SU']                 #1 8
store = []                                                  #1 0
for  i in range(t):                                         #n 1
    total_berth,seat_num = input().split(' ')               #n 2 
    total_berth,seat_num = int(total_berth),int(seat_num)   #n 0
    if total_berth>=seat_num:
        if seat_num%8==0:                                   #n 0
            store.append(berth[-1])                         #n n
        else:
            store.append(berth[(seat_num%8)-1])             #n n
    else:
        store.append('Invalid')
for each in store:                                          #n 1
    print(each)                                             #n 0

# T = 3+9n----->O(n)    S = 13+2n------>O(n)
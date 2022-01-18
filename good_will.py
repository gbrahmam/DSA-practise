n = int(input())                                                     #1  1
# space = ' '
dolar_box = '$*'   #even                                             #1  1
# star = '*'    
star_box = '*$'   #odd                                               #1  1
i=1                                                                  #1  1
while i<=n:                                                          #n  1
    # val = (2*i)-1                                                    
    if i%2 != 0:                                                     #n/2 0
        print((n-i)*(' ') + (i-1)*(star_box) + '*' + (n-i)*(' '))    #n/2 0
    
    elif i%2 == 0:                                                   #n/2 0
        print((n-i)*(' ') + (i-1)*(dolar_box) + '$' + (n-i)*(' '))   #n/2 0
    i+=1                                                             #n 1

# T = 4+4n----->O(n)     S = 5------> O(1)
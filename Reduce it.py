def reduceit(n):                                            #75%
    if n%2!=0 and n>0:
        return reduceit(n-21)
    elif n%2==0 and n>=0:
        return reduceit(n-11)
    else:
        return n
n = int(input())
print(reduceit(n))


                                                                                   #Approach2

num = int(input())                                  #100%
while num>0:
    if num%2==0:
        num-=11
    else:
        num-=21
print(num)
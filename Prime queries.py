                                                                   #more than 1sec

import math
#makes primes in range upto N_max
def sieve(N):
    prime = [True for x in range(N+1)]
    prime[0],prime[1] = False,False
    # print(prime)
    i = 2
    while i<(math.sqrt(N)+1):
        for i_mult in range(i**2,N,i):
            if prime[i_mult]==True:
                prime[i_mult]=False
        i+=1
        # print(i)
    return prime

#for each query return the count of primes
def QUERY(arr,n):
    count = 0
    for idx in range(n+1):
        if arr[idx]==True:
            count+=1
    return count

#user inputs
N_max,q = [int(i) for i in input().split()]
Arr = sieve(N_max)
# print(Arr)
for each in range(q):
    val = int(input())
    print(QUERY(Arr,val))

                                                                         #O(N*log(logN))---less than 1sec

import math
#makes primes in range upto N_max
def sieve(N):
    prime = [True for x in range(N+1)]
    prime[0],prime[1] = False,False
    # print(prime)
    i = 2
    while i<(math.sqrt(N)+1):
        if prime[i]==True:
            for i_mult in range(i**2,N,i):
                    prime[i_mult]=False
        i+=1
        # print(i)
    return prime

#user inputs
N_max,q = [int(i) for i in input().split()]
Arr = sieve(N_max)
# print(Arr)
# queries = []
res = 0
for i in range(len(Arr)):
    if Arr[i]==False:
        Arr[i]=res
    elif Arr[i]==True:
        res+=1
        Arr[i]=res
# print(Arr)
for each in range(q):
    # query = int(input())
    print(Arr[int(input())])
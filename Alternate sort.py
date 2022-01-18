n = int(input())
store = []
for i in range(n):
    
    Arr = [int(i) for i in input().split(' ')]
    
    ev_arr = []

    odd_arr = []

    for i in range(len(Arr)):
    
        if i%2==0:
            ev_arr.append(Arr[i])
        else:
            odd_arr.append(Arr[i])


    for i in range(len(ev_arr)):
    
        for j in range(len(ev_arr)):
        
            if ev_arr[i]>ev_arr[j]:
                ev_arr[i],ev_arr[j] = ev_arr[j],ev_arr[i]
            
    # print(ev_arr)


    for i in range(len(odd_arr)):
    
        for j in range(len(odd_arr)):
        
            if odd_arr[i]<odd_arr[j]:
                odd_arr[i],odd_arr[j] = odd_arr[j],odd_arr[i]
            
    # print(odd_arr)

    for i in range(0,len(Arr),2):
        Arr[i] = ev_arr[i//2]
    
    for i in range(1,len(Arr),2):
        Arr[i] = odd_arr[i//2]
    
    # print(Arr)
    store.append(Arr)

for i in range(len(store)):
    
    for j in range(len(store[i])):
        
        print(store[i][j],end=' ')
    
    print()


                                                                          #APPROACCH#2 (6.57SEC)

def insertiontSort(A,n):
    insertionAsc(A,n)
    insertionDsc(A,n)
    return A
    
def insertionDsc(A,n):
    
    for i in range(2,n,2):
        key = A[i]
        while i>1 and key>A[i-2]:
            A[i]=A[i-2]
            i-=2
        A[i]=key
    return

def insertionAsc(A,n):
    
    for i in range(3,n,2):
        key = A[i]
        while i>2 and key<A[i-2]:
            A[i]=A[i-2]
            i-=2
        A[i]=key
    return

t = int(input())
for i in range(t):
    Arr = [int(i) for i in input().split(' ')]
    store = insertiontSort(Arr,len(Arr))
    for each in store:
        print(each,end=' ')
    
    
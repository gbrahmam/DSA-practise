def insertionaltSort(A, n):
    
    for i in range(2,n):
        key_ele = A[i]
    
        while i>1 and key_ele<A[i-2]:
                
            A[i] = A[i-2]
            # key_ele = A[i-1]
            i-=2
        A[i] = key_ele
    
    return A

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*insertionaltSort(arr, n))
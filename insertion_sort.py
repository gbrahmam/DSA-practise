def insertionSort(A, n):
    
    for i in range(1,n):
        key_ele = A[i]
    
        while i>0 and key_ele<A[i-1]:
                
            A[i] = A[i-1]
            # key_ele = A[i-1]
            i-=1
        A[i] = key_ele
    
    return A

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*insertionSort(arr, n))
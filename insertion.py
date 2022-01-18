def insert(arr,n):
    # Your code goes here
    if n == 1:
        return
    for i in range(1,n):
        if arr[i-1]<=arr[i]:
            pass
        else:
            break
    if i == n-1:
        return
    else:
        store = i
    
    for j in range(store,n):
        key = arr[j]
        
        while j>0 and key<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j] = key
    
    return

### DO NOT EDIT ANYTHING BELOW THIS LINE

if __name__=='__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    insert(arr, n)
    print(*arr)
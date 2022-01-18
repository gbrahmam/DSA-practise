def mergeSort(arr, left, right):
    if right > left:
        mid = (left + right) // 2

        mergeSort(arr, left, mid) # left half

        mergeSort(arr, mid + 1, right) # right half

        merge(arr, left, mid, right) # merging 2 halves left...mid & mid+1...right

def merge(arr, left, mid, right): # magic happens here
    i = left
    j = mid + 1

    tmp = [0] * (right - left + 1)
    k = 0

    while i <= mid and j <= right: # iterate while any of sub-array reaches last
        if arr[i] >= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1

        k += 1

    while i <= mid: # copy remaining element from 1st half if any
        tmp[k] = arr[i]
        k += 1
        i += 1

    while j <= right: # copy remaining element from 2nd half if any
        tmp[k] = arr[j]
        k += 1
        j += 1

    l = left

    for t in tmp: # copy merged sorted tmp back to arr
        arr[l] = t
        l += 1

q,k = input().split()
q,k = int(q),int(k)

time = [int(x) for x in input().split()[0:q]]
score = [int(x) for x in input().split()[0:q]]

mergeSort(time, 0, len(time) - 1)

for i in range(1,q):
    time[i] = time[i-1]+time[i]

# print(time)

for j in range(k):
    print(time[int(input())-1])
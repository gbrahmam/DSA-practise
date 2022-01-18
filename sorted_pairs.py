# your code goes here
def inversionCount(arr, left, right):
    invCount = 0

    if right > left:
        mid = (left + right) // 2

        invCount += inversionCount(arr, left, mid)

        invCount += inversionCount(arr, mid + 1, right)

        invCount += merge(arr, left, mid, right)

    return invCount

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = 0
    invCount = 0

    tmp = [0] * (right - left + 1)

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
        if i<j and arr[i] <= arr[j]:
            # print('('+str(arr[i])+','+str(arr[j])+')')
            invCount+=(right - j + 1)
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1

    l = left

    for t in tmp:
        arr[l] = t
        l += 1

    return invCount

n = int(input())
Arr = [int(x) for x in input().split()[0:n]]
print(inversionCount(Arr, 0, len(Arr) - 1))
# print(Arr) 
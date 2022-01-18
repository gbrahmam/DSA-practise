t = int(input())

for i in range(t):
    Arr =[int(x) for x in input().split()]
    Arr.sort(reverse = True)
    flag = True
    for i in range(2,len(Arr)):
        if Arr[i]+Arr[i-1]>Arr[i-2] and Arr[i-1]+Arr[i-2]>Arr[i] and Arr[i-2]+Arr[i]>Arr[i-1]:
            flag = False
            perimeter = Arr[i]+Arr[i-1]+Arr[i-2]
            break
    if flag == False:
        print(perimeter)
    else:
        print(0)
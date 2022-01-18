# your code goes here
for i in range(int(input())):
    n = int(input())
    step = input()
    Arr =[]
    for char in step:
        if char == 'U':
            Arr.append(1)
        elif char == 'D':
            Arr.append(-1)
    for i in range(1,n):
        Arr[i] = Arr[i-1]+Arr[i]
    # print(Arr)
    count = 0
    i = 0
    start = 0
    while i<n:
        if Arr[i]==-1:
            # print(i)
            for j in range(i+1,n):
                if Arr[j]==0:
                    i = j
                    count+=1
                    break
        i+=1
    print(count)
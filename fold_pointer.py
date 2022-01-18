n = int(input())
n_c = n
Arr1 = []                                          
for i in range(n):           
    Arr1.append(int(input()))
total_fold = int(input())

if total_fold == 0:
    print(len(Arr1))
    for i in range(n):
        print(Arr1[i])
else:
    
    fold_count = 0

    i = 0
    j = n-1
    # print('initial array')
    # print(Arr1)
    while fold_count<total_fold:
        if n_c%2 == 0:
            mid_pointer = n_c//2               #finding end pointer for next fold
        else:
            mid_pointer = n_c//2+1
        n_c = mid_pointer
    
        while j>i:
            Arr1[i] = Arr1[i]+Arr1[j]
            i+=1
            j-=1
        j = mid_pointer-1                  #updating end pointer
        i = 0                              # setting back start pointer
        fold_count+=1
        # print('aar1 after', fold_count)
        # print(Arr1)
        # print('total elements after', fold_count)
        # print(mid_pointer)
        # print('===========')
    
    print(mid_pointer)
    for i in range(mid_pointer):
        print(Arr1[i])
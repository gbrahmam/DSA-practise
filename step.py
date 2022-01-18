n = int(input())
if n>=1 and n<=100000:
    Arr1 = [int(x) for x in input().split(' ')]
    total=0
    max_ele = -1
    for i in range(n-1,-1,-1):
        max_ele = max(max_ele,Arr1[i])
        step_scr = max_ele - Arr1[i]
        total+=step_scr
        # print(i)
        # print(max_ele,'####')
    # if total == 0:
    #     print(total)
    # else:
    print(total)




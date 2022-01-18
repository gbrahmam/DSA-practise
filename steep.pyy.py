n = int(input())
Arr2 =[]
if n>=1 and n<=10**5:
    Arr1 = [int(x) for x in input().split()[0:n]]
    i = 0
    while i<=n:
        max_ele = max(Arr1[i:n])
        step_scr = max_ele - (Arr1[i])
        Arr2.append(step_scr)
        # total+=step_scr
        # print(max_ele, step_scr)
        i+=1
    print(Arr2)
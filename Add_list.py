n = int(input())
for i in range(n):
    Arr1 = [int(x) for x in input().split()]
    Arr2 = [int(x) for x in input().split()]
    if len(Arr2)>len(Arr1):
        Arr1,Arr2 = Arr2,Arr1
    summ = 0
    cary = 0
    Arr3 = []
    for i in range(len(Arr2)):
        summ = Arr1[i]+Arr2[i]+cary
        cary = summ//10
        Arr3.append(summ%10)
    for i in range(len(Arr2),len(Arr1)):
        summ = Arr1[i]+cary
        cary = summ//10
        Arr3.append(summ%10)
    if cary!=0:
        Arr3.append(cary)
    
    for each in Arr3:
        print(each,end='')
    print()
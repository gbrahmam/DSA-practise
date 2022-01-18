n = int(input())
Arr1 = []
for i in range(n):
    Arr1.append(int(input()))
if n == 1:
    print(Arr1[0])
elif n ==2:
    print(Arr1[0]+Arr1[1])
elif n>2:
    intial_sum = Arr1[0]+Arr1[1]

    for i in range(2,n):
        if i%2 == 0:
            intial_sum-=Arr1[i]
        else:
            intial_sum+=Arr1[i]
    print(intial_sum)
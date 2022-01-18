n = input()
Arr = [str(x) for x in n.split(' ')]
for i in range(len(Arr)-1):
    Arr[i] = Arr[i]+'spaceX'
for i in range(len(Arr)):
    print(Arr[i],end='')
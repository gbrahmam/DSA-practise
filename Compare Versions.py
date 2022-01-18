# your code goes here
t = int(input())
for i in range(t):
    version = [x for x in input().split()]
    ver1 = [int(x) for x in version[0].split('.')]
    ver2 = [int(x) for x in version[1].split('.')]
    
    if len(ver2)>len(ver1):
        ver1+=(len(ver2)-len(ver1))*[0]
    else:
        ver2+=(len(ver1)-len(ver2))*[0]
    flag = True
    # print(ver1, ver2)
    for i in range(len(ver1)):
        if ver1[i]>ver2[i]:
            flag = False
            print(1)
            break
        elif ver1[i]<ver2[i]:
            flag = False
            print(-1)
            break
    if flag == True:
        print(0)
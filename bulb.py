n = int(input())
flag = 'OFF'
count = 0
for i in range(n):
    status = input()
    
    if status == 'ON':
        if flag == 'OFF':
            flag = status
            count+=1
        else:
            flag = status
    elif status == 'OFF':
        flag = status
    elif status == 'Toggle':
        if flag == 'OFF':
            flag = 'ON'
            count+=1
        else:
            flag = 'OFF'
print(count)
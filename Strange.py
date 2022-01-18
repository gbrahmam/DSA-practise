def strange(n):
    if n<10:
        return True
    add = 0
    prod = 1
    while n!=0:
        dig = n%10
        n = n//10
        add+=dig
        prod*=dig
    if add>=prod:
        return True
    else:
        return False
    
count = 0
for i in range(int(input())):
    res = strange(int(input()))
    if res == True:
        count+=1
print(count)
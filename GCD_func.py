def GCD(a,b):
    
    if a<b:
        a,b = b,a
    
    if a%b == 0:
        return b
    else:
        temp = a
        a = b
        b = temp%b
        return GCD(a,b)
        
n = int(input())
store = []
for i in range(n):
    inp_arr = [int(x) for x in input().split(' ')[0:2]]
    res = GCD(inp_arr[0],inp_arr[1])
    store.append(res)
    
for each in store:
    print(each)
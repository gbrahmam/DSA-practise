def handle_str(strng):
    length = len(strng)
    
    if length%3 == 0 and length%5 == 0:
        return ('foobar')
    
    elif length%3 == 0:
        return('foo')
        
    elif length%5 == 0:
        return('bar')
    
    else:
        return ('-')
        
n = int(input())
store =[]
for i in range(n):
    inp_str = input()
    res = handle_str(inp_str)
    store.append(res)

for each in store:
    print(each)
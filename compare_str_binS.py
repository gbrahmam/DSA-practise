def strchange(svar,idx):                                          #60%(with out BinSearch)
    arr=list(svar)
    arr[idx-1]=1
    return ''.join(str(x) for x in arr)

N,Q = input().split()
str_A = input()
str_B = input()
mod_str = str_B
for each in range(int(Q)):
    pos = int(input())
    mod_str = strchange(mod_str,pos)
    if mod_str>=str_A:
        print('YES')
    else:
        print('NO')
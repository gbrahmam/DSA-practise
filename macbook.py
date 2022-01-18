def macbook(n,res =0):
    if n==0:
        return res
    val = int(input())
    if val>0:
        res+=val
    return macbook(n-1,res)

n = int(input())
print(macbook(n))
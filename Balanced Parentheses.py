def mkpar(n,op,cl,pos,svar,pairs):
    if cl == 0 and op == 0:
        pairs.append(svar)
        return
    
    if op!=0:
        svar_1 = svar+'('
        mkpar(n,op-1,cl,pos+1,svar_1,pairs)
    
    if cl>op:
        svar_2 = svar+')'
        mkpar(n,op,cl-1,pos+1,svar_2,pairs)

def getAllBalancedParan(n):
    # Implement this function
    pairs = []
    mkpar(n,n,n,0,'',pairs)
    return pairs

# Do not edit anything below
n = int(input())
allBalancedParan = getAllBalancedParan(n)
allBalancedParan.sort()
for expr in allBalancedParan:
    print(expr)
def palcheck(svar):
    
    if len(svar) == 1:
        return True
    i = 0
    j = len(svar)-1
    
    while svar[i]==svar[j]:
        i+=1
        j-=1
        if i==(len(svar)//2):
            return True
    #removing the right/left mismatch char and chk if pal
    if svar[i:j:1] == svar[j-1:i-1:-1] or svar[i+1:j+1:1]==svar[j:i:-1]:
        return True
    
    return False

for i in range(int(input())):
    svar = input()
    print(palcheck(svar))
def palinrecur(Arr,n,newstring):
    #base case
    if n==0:
        if newstring == oldstring:
            return (True)
        else:
            return (False)
    
    
    newstring+=Arr.pop()
    
    #normal case
    return palinrecur(Arr,len(Arr),newstring)


for i in range(int(input())):
    newstring = ''
    oldstring = input()
    Arr = list(oldstring)
    print(palinrecur(Arr,len(oldstring),newstring))
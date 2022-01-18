def revstr(string,n):
    
    if n<0:
        return newstring
    
    char = string[n]
    newstring.append(char)
    
    return revstr(string,n-1)

t = int(input())

for i in range(t):
    newstring= []
    string = input()
    n = len(string)-1
    newstring = revstr(string,n)
    for each in newstring:
        print(each,end='')
    print()
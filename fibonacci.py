#return n terms of fibonacci series
#req is do it iteratively
def getfibo(n):
    Arr1 = [0,1]                  #1 2
    ele1 = 0                      #1 1
    ele2 = 1                      #1 1

    for i in range(n):            #n 1
        summ=ele1+ele2            #n 1
        ele1=ele2                 #n 0
        ele2=summ                 #n 0
        Arr1.append(summ)         #n n
    return Arr1                   #1 0

print(getfibo(10))                #1 0

# S = 6+n--->O(n)     T = 5+5n




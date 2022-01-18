lst = [0,1,1,1,0,1,0,0,1,1]
i = 0
j = len(lst)-1
if len(lst)%2==0:
    while j>=(len(lst)//2):
        if lst[i]==0:
            i+=1
        if lst[j]==1:
            j-=1
        if lst[i]==1 and lst[j]==0:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
            j-=1
    print(lst)
elif len(lst)%2!=0:
    while j>(len(lst)//2):
        if lst[i]==0:
            i+=1
        if lst[j]==1:
            j-=1
        if lst[i]==1 and lst[j]==0:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
            j-=1
    print(lst)
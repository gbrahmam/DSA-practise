def onecount(val):
    count = 0
    while(val!=0):
        val &=(val-1)
        count+=1
    
    return count

tot_val = int(input())
values = [int(x) for x in input().split()]

values.sort(key = onecount, reverse = True)

print(*values)
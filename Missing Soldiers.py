barriers = set()
number_barriers = int(input())
for i in range(number_barriers):
    start,end,width = [int(x) for x in input().split()]
    for point in range(start,start+width+1):
        barriers.add(point)
print(len(barriers))

                                                              #Approach 2
                                                            
# your code goes here
tot_bar = int(input())
bar = []
for idx in range(tot_bar):
    x,y,width = [int(i) for i in input().split()]
    bar.append([x,x+width])
bar.sort()
stop = (bar[0][1] - bar[0][0])+1
right = bar[0][1]
for i in range(1,tot_bar):
    
    if bar[i][0] >right:
        stop+=(bar[i][1] - bar[i][0]) + 1
        right = bar[i][1]
    else:
        if bar[i][1]>right:
            stop+=(bar[i][1] - right)
            right = bar[i][1]

print(stop)
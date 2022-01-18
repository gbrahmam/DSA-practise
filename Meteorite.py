test_cases = int(input())

for idx in range(test_cases):
    n,m,tot_meteo = [int(i) for i in input().split()]
    x_coor = set()
    y_coor = set()
    x_coor.add(1)
    x_coor.add(n)
    y_coor.add(1)
    y_coor.add(m)
    for idx in range(tot_meteo):
        x,y = [int(i) for i in input().split()]
        x_coor.add(x)
        y_coor.add(y)
    
    # partitions = len(x_coor)*len(y_coor)
    x_parts = sorted(x_coor)
    y_parts = sorted(y_coor)
    x_div=[]
    for i in range(1,len(x_parts)):
        x_div.append(x_parts[i]-x_parts[i-1])
    y_div = []
    for j in range(1,len(y_parts)):
        y_div.append(y_parts[j]-y_parts[j-1])
    partitions = len(x_div)*len(y_div)
    min_area = min(x_div)*min(y_div)
    max_area = max(x_div)*max(y_div)
    
    print(partitions, min_area, max_area)
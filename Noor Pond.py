# your code goes here
test_cases = int(input())
for each in range(test_cases):
    tot_fish = int(input())
    f_size = []
    f_eat = []
    for fish in range(tot_fish):
        S,E = [int(x) for x in input().split()]
        f_size.append(S)
        f_eat.append(E)
    
    f_size.sort()
    f_eat.sort()
    s = 0
    e = 0
    f_count = 1
    while e<tot_fish:
        if f_eat[e]>=f_size[s]:
            f_count = max(f_count,(e-s))
            s+=1
        else:
            e+=1
    f_count = max(f_count,(e-s))
    print(f_count)
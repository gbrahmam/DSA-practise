test_cases = int(input())
for each in range(test_cases):
    tot_ppl = int(input())
    time_count ={}
    for ppl in range(tot_ppl):
        time = input()
        if time not in time_count:
            time_count[time]=1
        else:
            time_count[time]+=1
    
    print(max(time_count.values()))
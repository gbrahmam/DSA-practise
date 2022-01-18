n = int(input())
Arr = []
for i in range(n):
    Arr.append(int(input()))
    
# rev_arr = []

# for i in range(n-1,-1,-1):
#     rev_arr.append(Arr[i])
    
leader_arr = []
prev_leader = float('-inf')
leader = 0
for i in range(n-1,-1,-1):
    leader = max(leader,Arr[i])
    
    if leader!=prev_leader:
        leader_arr.append(leader)
        prev_leader = leader
    
for each in leader_arr:
    print(each)
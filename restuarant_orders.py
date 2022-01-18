n = int(input())
t = int(input())

table = []
amount = []

for i in range(n):
    table.append(int(input()))

for i in range(n):
    amount.append(int(input()))

costs = [0]*t

for i in range(n):
    costs[table[i]-1]+=amount[i]

max_cost = max(costs)
for i in range(len(costs)):
    if costs[i]==max_cost:
        print(i+1)
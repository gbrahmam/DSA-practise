elements = int(input())
perms = [int(x) for x in input().split()]

min_arr = []
max_arr = []
beauty = 0
for i in range(elements):
    beauty+=abs(perms[i]-(i+1))
    min_arr.append(min(i+1,perms[i]))
    max_arr.append(max(i+1,perms[i]))

beauty+= abs((min(max_arr) - max(min_arr))*2)

print(beauty)
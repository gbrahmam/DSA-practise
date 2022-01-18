n = int(input())            # 1  1
Income = []                 # 1  0
for i in range(n):          # n  1
    val = int(input())      # n  1
    Income.append(val)      # n  n
child = []                  # 1  0
for i in range(n):          # n  1
    val = int(input())      # n  1
    child.append(val)       # n  n
count = 0                   # 1  1
summ = 0                    # 1  1
for i in range(n):          # n  1
    if child[i]>2:          # n  0  Worst case scenario
        summ+=Income[i]     # n  0
        count+=1            # n  0
if summ == 0:
    print(-1)
else:
    print(summ//count)          # 1  0
# T = 6+10n---->O(n)    S = 8+2n------> O(n)
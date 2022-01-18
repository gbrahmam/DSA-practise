n = int(input())
count = 0
for i in range(n):
    m = len(input())
    if m%2!=0:
        count+=1
print(count)
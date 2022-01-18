n = int(input())

summ = 0

for i in range(n):
    summ+=int(input())
    
print(summ//n)

if (summ//n) <25:
    print(True)
else:
    print(False)
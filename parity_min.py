n = int(input())
Arr1 = []
for i in range(n):
    Arr1.append(int(input()))
min_val = min(Arr1)

str_val = str(min_val)
summ = 0
for char in str_val:
    summ+=int(char)
if summ%2 == 0:
    print(1)
else:
    print(0)
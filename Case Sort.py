n = int(input())
svar = input()
upper = []
lower = []

for char in svar:
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)

upper.sort()
lower.sort()

i=0
j=0
res = ''
for each in svar:
    if each.islower():
       res+=lower[i]
       i+=1
    elif each.isupper():
        res+=upper[j]
        j+=1

print(res)
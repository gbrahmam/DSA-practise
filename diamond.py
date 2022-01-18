n = int(input())
space = ' '
star = '*'
i=1

while i<=n-1:
    val = (2*i)-1
    print((n-i)*(space) + (star*val) + (n-i)*(space))
    i+=1

print(star*(2*n-1))

i=n-1
while i>=1:
    val = (2*i)-1
    print((n-i)*(space) + (star*val) + (n-i)*(space))
    i-=1



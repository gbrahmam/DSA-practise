def trailingZeroes(n):
    # WRITE YOUR CODE HERE
    if n<5:
        return 0
    res = 0
    while n!=0:
        res+=n//5
        n=n//5
    return res
 
# DO NOT CHANGE ANYTHING BELOW THIS LINE
num_tests=int(input())
for _ in range(num_tests):
    n=int(input())
    print(trailingZeroes(n))
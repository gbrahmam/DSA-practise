def sumOfFirstN(n):
    # Implement this function
    
    if n==0:
        return 0
    if n>0:
        summ = n + sumOfFirstN(n-1)
        print(n,end=' ')
        print(summ)
        return summ

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    sumOfFirstN(n)
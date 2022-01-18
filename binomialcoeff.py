def binomialCoeff(n, r):
    # Implement this function
    if r==0 or r==n:
        return 1
    else:
        return (binomialCoeff(n-1,r) + binomialCoeff(n-1,r-1))

# Do not edit anything below
if __name__ == "__main__":
    numTcs = int(input())
    for index in range(numTcs):
        inputInts = input().split(' ')
        n = int(inputInts[0])
        r = int(inputInts[1])
        print(binomialCoeff(n, r))
def cutRope(A):
    # Complete this function
    n = len(A)
    temp = []
    count = 0
    while count!=n:
        val =min(A)
        for i in range(n):
            res = A[i]-val
            if res==0:
                count+=1
                A[i] = float('inf')
            else:
                A[i]=res
        if count<n:
            temp.append(n-count)
    return temp

# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    for _ in range(int(input())):
        input_numbers.append(int(input()))

    for i in cutRope(input_numbers):
        print(i)


                                                                              #Approach2

def cutRope(A):
    # Complete this function
    A.sort()
    temp = []
    i=0
    j=0
    while i <len(A)-1:
        min_val = A[i]
        if A[i+1] - min_val==0:
           pass
        elif A[i+1] - min_val!=0:
           temp.append(len(A)-(i+1))
        i+=1
    return temp
# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    for _ in range(int(input())):
        input_numbers.append(int(input()))

    for i in cutRope(input_numbers):
        print(i)
#prod of 2's

def equation(arr):
    arr = [abs(i) for i in arr]
    arr_sqr = [i ** 2 for i in arr]
    return (sum(arr) ** 2 - sum(arr_sqr)) // 2
N = int(input())
num = [int(i) for i in input().split()]
print(str(equation(num)))



#breaking records
# your code goes here
# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini = scores[0]
    maxi = scores[0]
    res = [0,0]
    for i in range(1,len(scores)):
        if scores[i]<mini:
            res[1] += 1
            mini = scores[i]
        elif scores[i]>maxi:
            res[0] += 1
            maxi = scores[i]
    return res
if _name_ == ‘_main_‘:
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(’ ’.join(map(str, result)))
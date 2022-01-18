# name your function as right_to_left_diagonal
def right_to_left_diagonal(lst):
    Arr1 = []
    for i in range(m-1,-1,-1):
        Arr1.append(lst[m-i-1][i])
    
    return Arr1

# Do not change anything below this line
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    [print(val) for val in out]
# name your function as change_diagonal and it should take list as input
def change_diagonal(lst):
    # Arr1 = []
    for i in range(val):
        if lst[i][i]<0:
            lst[i][i] = 0
        elif lst[i][i]>=0:
            lst[i][i] = 1
    return lst

# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        print(" ".join(str(i) for i in lst1))
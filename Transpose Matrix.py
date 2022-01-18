# name you function as transpose_matrix and takes a list
# you should return a list of lists
def transpose_matrix(lst):
    m = len(lst)
    n = len(lst[0])
    Aux = [[0 for j in range(m)] for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            Aux[i][j] = lst[j][i]

    return Aux

# do not change anything below this line
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])
    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))
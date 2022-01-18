n = int(input())
m = int(input())
A = [abs(int(x)) for x in input().split()[0:n]]
B = [abs(int(x)) for x in input().split()[0:m]]

# A_max = max(A)
# B_max = max(B)

print(max(A) * max(B))
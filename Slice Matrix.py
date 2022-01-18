rows,column = input().split()
rows,column = int(rows),int(column)
matrix = []

for i in range(0,rows):
    matrix.append([int(x) for x in input().split(' ')])

left,right,top,bottom = input().split()
left,right,top,bottom = int(left),int(right),int(top),int(bottom)

for i in range(top-1,bottom):
    
    for j in range(left-1,right):
        
        print(matrix[i][j],end=' ')
    
    print()
# your code goes here
                                                                   #Grades
# Complete the ‘gradingStudents’ function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if(grades[i]<38):
            continue
        elif((grades[i]//5 + 1)*(5) - grades[i] < 3):
            grades[i] = (grades[i]//5 + 1)*(5)
    return grades
if _name_ == ‘_main_‘:
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    for i in result:
        print(i)



#Array rotation

# your code goes here
def rotate_right_K(arr, K):
    K = K % len(arr)
    left = arr[:len(arr) - K]
    right = arr[len(arr) - K:]
    arr = right + left
    for i in arr:
        print(str(i) + ” “)
N, Q = [int(i) for i in input().split()]
num = [int(i) for i in input().split()]
rot = 0
for _ in range(Q):
    Op, mod = input().split()
    mod = int(mod)
    if Op == ‘R’:
        rot += mod
    else:
        rot -= mod
rotate_right_K(num, rot)
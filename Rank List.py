# your code goes here
total_stud = int(input())

marks_list = []

for i in range(total_stud):
    name,scholar,marks = input().split()
    marks_list.append([name,int(scholar),int(marks)])

marks_list.sort(key = lambda x:x[1])
marks_list.sort(key = lambda x:x[0])
marks_list.sort(key = lambda x:x[2], reverse = True)

for i in range(total_stud):
    for idx in range(3):
        print(marks_list[i][idx],end=' ')
    print()
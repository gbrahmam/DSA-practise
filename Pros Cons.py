test_cases = int(input())
for each in range(test_cases):
    parameters = []
    total_girls = int(input())
    for girl in range(total_girls):
        parameters.append([int(x) for x in input().split()])
    parameters.sort(key=lambda x:x[0]+x[1], reverse=True)

    total_anger = 0
    for girl in range (total_girls):
        total_anger+=parameters[girl][1]
    
    print(parameters[0][0]+parameters[1][0]+parameters[0][1]+parameters[1][1] - total_anger)




test_cases = int(input())
for each in range(test_cases):
    parameters = []
    total_anger = 0
    total_girls = int(input())
    for girl in range(total_girls):
        fav,unfav = (int(x) for x in input().split())
        parameters.append(fav+unfav)
        total_anger+=unfav
    parameters.sort(reverse=True)
    print(parameters[0]+parameters[1] - total_anger)
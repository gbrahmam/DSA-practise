# your code goes here
test_cases = int(input())

for idx in range(test_cases):
    num_ele = int(input())
    elem = [int(x) for x in input().split()]
    
    max_ele = max(elem)
    min_ele = min(elem)
    
    if max_ele == elem[0] and min_ele == elem[num_ele-1]:
        elem.sort()
        res = max((max_ele - elem[1]),(elem[-2] - min_ele))
    else:
        res = max_ele - min_ele
    
    print(res)
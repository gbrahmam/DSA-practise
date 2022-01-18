# your code goes here
test_cases = int(input())
for i in range(test_cases):
    tot_boxes = int(input())
    boxes =[int(x) for x in input().split()]
    val = tot_boxes-1
    boxes.sort(reverse=True)
    add =0
    for i in range(tot_boxes):
        add+=boxes[i]*val
        val-=2
    print((max(tot_boxes)*add)%(1000000007))
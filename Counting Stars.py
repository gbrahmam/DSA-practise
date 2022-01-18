from collections import defaultdict

for i in range(int(input())):
    
    n = int(input())
    star = list(input())
    # print(star)
    d = dict.fromkeys(star,-1)
    summ = dict.fromkeys(star,0)
    for each in star:
        d[each]+=1
        summ[each]+=d[each]
    # print(d)
    # print(summ)
    total=0
    for each in summ:
        total+=summ[each]
    print(total)


                                                                           #approach2
    
    from collections import defaultdict

for i in range(int(input())):
    
    n = int(input())
    star = list(input())
    # print(star)
    d = dict.fromkeys(star,-1)
    summ = 0
    # summ = dict.fromkeys(star,0)
    for each in star:
        d[each]+=1
        summ+=d[each]
    # print(d)
    # print(summ)
    # total=0
    # for each in summ:
    #     total+=summ[each]
    print(summ)
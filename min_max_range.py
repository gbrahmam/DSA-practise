def maximum_value(input_numbers):                                                 #1  0
    # write below this here 
    maximum = list2[0]                                                            #1  1
    for each in list2:                                                            #n  1  
        if each>maximum:                                                          #n  n  worst case
            maximum = each                                                        #n  0
    return maximum                                                                #1  0
## This function should return single integer. 
## The integer should be minimum value of input list
def minimum_value(input_numbers):                                                 #1  0
    # Please write below this  
    minimum = list1[0]                                                            #1  1
    for each in list1:                                                            #n  1
        if each<minimum:                                                          #n  n   worst case
            minimum = each                                                        #n  n
    return minimum                                                                #1  0
## This function should return list of integer which lies between m1 and m2. 
## if m1 <= m2 return list off numbers between m1 and m2
## if m2 <= m1 return list off numbers between m2 and m1
def get_numbers_in_range(input_numbers, m1, m2):                                  #1  0
    # Please write below this line 
    # list3 = [int(i) for i in input().split(' ')]
    # minimum = 3
    # maximum = 23
    list4 = []                                                                    #1  0
    if m1>m2:                                                                     #1  0  worst case 
        m1,m2 = m2,m1                                                             #1  0
    
    for each in list3:                                                            #n  1  
        if each>=m1 and each<=m2:                                                 #n  0  worst case  
            list4.append(each)                                                    #n  0
    if list4 == []:                                                               #1  0
        # print([-1]) 
        return ([-1])                                                             #1  0
    else:                                                                          
        # print(list4)
        return (list4)

### Please do not change anything below this line.
if __name__ == "__main__":
    list1 = [int(i) for i in input().split(' ')]
    list2 = [int(i) for i in input().split(' ')]
    list3 = [int(i) for i in input().split(' ')]
    m1 = minimum_value(list1)
    m2 = maximum_value(list2)
    min_max_range = get_numbers_in_range(list3, m1, m2)
    [print(i) for i in min_max_range]

# T = 12+9n----->O(n)      S = 5+3n------>O(n)
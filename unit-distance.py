def isEditDistanceOne(string1, string2): 
    # Complete this function, and return True/False
    if len(string2)>=len(string1):
        primary_str = string2
        secondary_str = string1
    else:
        primary_str = string1
        secondary_str = string2
    
    if int(len(primary_str)-len(secondary_str))>1:
        return False
    
    i = 0
    j = 0
    count = 0
    while (i<len(secondary_str)):
        if secondary_str[i]!=primary_str[j]:
            count+=1
            if j+1<len(primary_str) and secondary_str[i]==primary_str[j+1]:
                j+=1
        if count>1:
            return False
        j+=1
        i+=1
    if j!=len(primary_str):
        count+=len(primary_str) - len(secondary_str)
    if count==1:
        return True
    else:
        return False
for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))
def findLuckyNumber(nums):
    # implement this function
    count = 1                                            
    flag = -1                                         
    if len(input_arr) == 1 and nums[0] == 1:
        return (input_arr[0])
    else:
        for i in range(1,num_elems):                         
            if input_arr[i] == input_arr[i-1]:               
                count+=1
            else:
                if count == input_arr[i-1]:
                    flag = input_arr[i-1]
                    break
                count = 1
            
        if count == input_arr[-1]:
            flag = input_arr[-1]
    
            
        # if flag == True:
        #     return input_arr[i-1]
        # else:
        #     return (-1)
        
        return flag
            

# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))
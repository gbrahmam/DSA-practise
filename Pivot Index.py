def pivotIndex(arr):
    
    if len(arr)==1:
        return 0
    
    if len(arr)==2:
        left_sum = 0
        right_sum = sum(arr[1:len(arr)])
        if left_sum == right_sum:
            return 0
    
        right_sum = 0
        left_sum = sum(arr[0:len(arr)-1])
        if right_sum == left_sum:
            return 1
        
        return -1
    
        
    if len(arr)>2:
        
        left_sum = 0                                 # first term
        right_sum = sum(arr[1:len(arr)])
        if left_sum == right_sum:
            return 0
        
        for i in range(1,len(arr)-1):               # middle terms
            left_sum = sum(arr[0:i])
            right_sum = sum(arr[i+1:len(arr)])
            
            if left_sum == right_sum:
                return i
        
        right_sum = 0                                # last term
        left_sum = sum(arr[0:len(arr)-1])
        if right_sum == left_sum:
            return (len(arr)-1)
            
        return -1
    

# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))





                                                                        #Approach2(less time)

def pivotIndex(arr):
    # Implement this function
    if len(arr)==1:
        return 0
    left = 0
    right = sum(arr)
    
    for i in range(n):
        right-=arr[i]
        if left == right:
            return i
        left+=arr[i]
    
    return -1
    
# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))



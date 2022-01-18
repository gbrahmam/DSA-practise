n = int(input())
Arr1 = []
# Arr2 = []
Arr3 = []
for i in range(2*n):
    Arr1.append(int(input()))
for i in range(n):
    Arr3.append(Arr1[i])
    Arr3.append(Arr1[n+i])    
for i in range(2*n):
    # print('==============')
    # print('         ')
    print(Arr3[i])


                                           #using definition

def shuffle(arr):
    # Implement this function
    Arr3=[]
    for i in range(n):
    	Arr3.append(nums[i])
    	Arr3.append(nums[n+i])
    return Arr3
    

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)

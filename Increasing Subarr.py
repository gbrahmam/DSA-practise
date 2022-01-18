n = int(input())

inp_Arr = [int(x) for x in input().split(' ')[0:n]]

curr_first_index = 0
last_index = 0
max_length = 1
counter = 1
first_index = 0
for i in range(1,n):
    if inp_Arr[i]>inp_Arr[i-1]:
        counter+=1
    else:
        if counter>max_length:
            max_length = counter
            last_index = i-1
            first_index = curr_first_index
        
        curr_first_index = i
        counter = 1
        
# if i == n-1:
if counter>max_length:
    max_length = counter
    last_index = i
    first_index = curr_first_index

print(max_length,end=' ')
print(first_index+1,end=' ')
print(last_index+1,end=' ')
def insertionSortAsc(arr) :
  for index in range(0, len(arr),2) :
    key = arr[index]
    prev_index = index-2
    while prev_index >= 0 and key < arr[prev_index] :
      arr[prev_index+2] = arr[prev_index]   
      prev_index = prev_index - 2
    arr[prev_index + 2] = key 

def insertionSortDesc(arr) :
  for index in range(1, len(arr),2) :
    key = arr[index]
    prev_index = index-2
    while prev_index >= 0 and key > arr[prev_index] :
      arr[prev_index+2] = arr[prev_index]   
      prev_index = prev_index - 2
    arr[prev_index + 2] = key 

arr = [2,4,-1,8,0,-3]
insertionSortAsc(arr)
insertionSortDesc(arr)
print(arr)
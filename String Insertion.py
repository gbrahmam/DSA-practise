def stringInsertionSort(string):
    # Your code goes here
    Arr = list(string)
    newstring=''
    for i in range(1,len(Arr)):
    
        key_char = Arr[i]
    
        while i >0 and key_char<Arr[i-1]:
            Arr[i] = Arr[i-1]
            i-=1
        Arr[i] = key_char
    
    for each in Arr:
        newstring+=each
    
    return newstring
    

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))
        
        
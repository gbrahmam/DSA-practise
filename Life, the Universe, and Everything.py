Arr = []                     #1 0
while True:                  #n 0
    val = int(input())       #n 1
    if val!=42:              #n 0
        Arr.append(val)      #n n 
    else:
        break
for each in Arr:             #n 1
    print(each)              #1 0

# T = 2+5n----->O(n)   S = 2+n------>O(n)
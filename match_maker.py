for i in range(int(input())):
    
    count = int(input())
    
    girl_list = [int(x) for x in input().split()[0:count]]
    
    boy_list = [int(x) for x in input().split()[0:count]]
    
    girl_list.sort()
    boy_list.sort(reverse = True)
    
    pair = 0
    
    for i in range(count):
        
        if girl_list[i]%boy_list[i]==0 or boy_list[i]%girl_list[i]==0:
            pair+=1
    
    print(pair)
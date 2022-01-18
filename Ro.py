def RoG(string):
    
    if len(string) == 0:
        return 0
        
    if len(string) == 1:
        
        if string == 'R':
            return 0
        elif string == 'G':
            return 0
        
    elif len(string)>1:
        
        r_count = 0
        g_count = 0
        
        for char in string:
            if char == 'R':
                r_count+=1
            else:
                g_count+=1
        
        return min(r_count,g_count)

string = input()

print(RoG(string))
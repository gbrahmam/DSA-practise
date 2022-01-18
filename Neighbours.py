def neighbour(n,arr,svar,pos,count):
    
    if pos == n:
        arr.append(svar)
        return
    
    if count == 0:
        neighbour(n,arr,svar+'a',pos+1,count+1)
        neighbour(n,arr,svar+'b',pos+1,count+1)
    
    if count == 1:
        
        if svar[-1] == 'a':
            neighbour(n,arr,svar+'a',pos+1,count+1)
            neighbour(n,arr,svar+'b',pos+1,count)
        else:
            neighbour(n,arr,svar+'a',pos+1,count)
            neighbour(n,arr,svar+'b',pos+1,count+1)
    
    if count == 2:
        
        if svar[-1]=='a':
            neighbour(n,arr,svar+'b',pos+1,1)
        else:
            neighbour(n,arr,svar+'a',pos+1,1)

panel = int(input())
panel_arr = []
neighbour(panel,panel_arr,'',0,0)
for each in panel_arr:
    print(each)
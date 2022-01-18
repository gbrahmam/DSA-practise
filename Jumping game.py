# your code goes here
def jumpgame(panel,jumps,pos,jump_arr):
    
    if pos>=len(panel):
        return jump_arr.append(jumps)
    
    jumpgame(panel,jumps+1,pos+1,jump_arr)
    
    jumpgame(panel,jumps+1,pos+panel[pos],jump_arr)

tot_panels = int(input())
panel = [int(i) for i in input().split()]
jumps = 0
jump_arr = []
jumpgame(panel,0,0,jump_arr)
print(min(jump_arr))
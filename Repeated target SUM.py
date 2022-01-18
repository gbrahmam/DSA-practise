def reptarSum(tar,arr,pos,curr,res):
    
    if tar == 0 and pos==len(arr)-1:
        if curr not in res:
            res.append(curr)
        return res
    
    if pos>len(arr)-1 or tar<0:
        return
    
    reptarSum(tar - arr[pos],arr,pos+1,curr+[arr[pos]],res)
    reptarSum(tar,arr,pos+1,curr,res)
    reptarSum(tar - arr[pos],arr,pos,curr+[arr[pos]],res)

tot_ele,key = [int(i) for i in input().split()]
elem = [int(x) for x in input().split()]
curr=[]
res = []
reptarSum(key,elem,0,curr,res)
print(len(res))
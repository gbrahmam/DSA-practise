def minele(arr,l,r,k):

    if l<=r:
        mid = (l+r)//2
        pot_mat = arr[mid]

        if k<=pot_mat:
            return minele(arr,mid+1,r,k)
        elif k>pot_mat:
            return minele(arr,l,mid-1,pot_mat)
        
    return k

n = int(input())
nums=[int(x) for x in input().split()]
curr_min = nums[0]
print(minele(nums,0,n-1,curr_min))
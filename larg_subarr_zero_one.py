class Solution:
    def maxLen(self,arr, N):
        # code here
        summ = 0
        maxSize = 0
        d = {0:-1}
        
        for i in range(0,n):
            if arr[i]==0:
                summ+=-1
            else:
                summ+=1
            
            if summ in d:
                length = i - d[summ]
                maxSize = max(length,maxSize)
            else:
                d[summ]=i
            
        return maxSize
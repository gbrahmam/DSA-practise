class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Arr =[]
        for i in range(1,len(prices)):
            Arr.append(prices[i]-prices[i-1])
        
        for i in range(1,len(Arr)):
            Arr[i] = max(Arr[i]+Arr[i-1],Arr[i])
        
        if max(Arr)<0:
            return 0
        else:
            return max(Arr)
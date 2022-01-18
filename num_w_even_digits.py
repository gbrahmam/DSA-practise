from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        self.nums = Arr1
        # n = len(self.nums)
        count = 0
        for each in self.nums:
            num_len = len(str(each))
            if num_len%2 == 0:
                count+=1
        return count
                
Arr1 = [int(x) for x in input().split()]
p1 = Solution()
print(p1.findNumbers(Arr1))
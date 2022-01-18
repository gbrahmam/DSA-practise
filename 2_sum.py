class Solution:
    def twoSum(self, nums, target):
        self.nums = Arr1
        self.target = key
        
        for i in range(len(self.nums)):
            j = i+1
            for k in range(j,len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]
        

Arr1 = [int(x) for x in input().split(' ')]
key = int(input())
p1 = Solution()
print(p1.twoSum(Arr1,key))




                                         #Sort----pointers---method


class Solution:
    def twoSum(self, nums, target):
        self.nums = Arr1
        Arr2 = Arr1.copy()
        self.target = key
        Arr2.sort()
        i = 0                     #start pointer
        j = len(self.nums)-1      #end pointer
        while j>i:
            if Arr2[i]+Arr2[j] == self.target:
                m,n = self.nums.index(Arr2[i]),self.nums.index(Arr2[j])
                break
            elif Arr2[i]+Arr2[j]<self.target:
                i+=1
            elif Arr2[i]+Arr2[j]>self.target:
                j-=1
        return [m,n]
        

Arr1 = [int(x) for x in input().split(' ')]
key = int(input())
p1 = Solution()
print(p1.twoSum(Arr1,key))
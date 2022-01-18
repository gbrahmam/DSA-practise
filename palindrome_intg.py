class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = False
        self.x = z
        int_str = str(self.x)
        check = int_str[-1::-1]
        if int_str == check:
            flag = True
        return flag

z = int(input())
p1 = Solution()
print(p1.isPalindrome(z))

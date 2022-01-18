class Solution:
    def mergeAlternately(self, word1, word2):
        self.word1 = str1
        self.word2 = str2
        len_1 = len(self.word1)
        len_2 = len(self.word2)
        # len_diff = abs(len_1 - len_2)
        k = min(len_1,len_2)
        new_str = ''
        
        for i in range(k):
            new_str+=self.word1[i]
            new_str+=self.word2[i]
        
        if len_1>len_2:
            for i in range(k,len_1):
                new_str+=self.word1[i]
        elif len_2>len_1:
            for i in range(k,len_2):
                new_str+=self.word2[i]
        
        return new_str
        
str1 = input()
str2 = input()

p1 = Solution()
print(p1.mergeAlternately(str1,str2))
print(type(p1.mergeAlternately(str1,str2)))
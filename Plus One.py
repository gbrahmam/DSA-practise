class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        val = digits[-1]+1
        carry = val//10
        arr.append(val%10)
        # print(arr)
        for idx in range(len(digits)-2, -1,-1):
            val= digits[idx]+carry
            carry = val//10
            arr.append(val%10)
        if carry!=0:
            arr.append(carry)
        # print(arr)
        res = []
        for i in range(len(arr)-1, -1,-1):
            res.append(arr[i])
        return res




class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        svar = ''
        for each in digits:
            svar+=str(each)
        num = int(svar)+1
        var = str(num)
        arr = []
        for each in var:
            arr.append(each)
        return arr
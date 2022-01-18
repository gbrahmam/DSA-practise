from collections import defaultdict
# import string
Arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# alpha = string.ascii_lowercase
# alphabet = list(alpha)
# # print(alphabet)

# d ={}
# for i in range(len(alphabet)):
#     d[alphabet[i]] = Arr[i]
# # print(d)

t = int(input())
for i in range(t):
    strarr = input().split()
    d2 = {}
    for word in strarr:
        morsecode=''
        for char in word:
            morsecode+=Arr[ord(char)- ord('a')]
        if morsecode not in d2:
            d2[morsecode]=1
    print(len(d2))
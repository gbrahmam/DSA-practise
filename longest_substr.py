# test_cases = int(input())
# for idx in range(test_cases):
#     svar = input()
#     if svar =='':
#         print(0)
#     else:    
#         res = ''
#         str_Arr = list(svar)
#         len_Arr = []
#         j = 0
#         while j<len(svar):
#             if str_Arr[j] not in res:
#                 res+=str_Arr[j]
#             else:
#                 len_Arr.append(len(res))
#                 res = ''
#                 j-=1
#             j+=1
#         # print(j)
#         if j==len(svar):
#             len_Arr.append(len(res))
#         # print(Arr2)
#         print(max(len_Arr))




test_cases = int(input())
for idx in range(test_cases):
    svar = input()
    char_d = {}
    max_lenstr = 0
    start = -1
    for idx in range(len(svar)):
        if svar[idx] in char_d:
            start = max(start,char_d[svar[idx]])
        max_lenstr = max(max_lenstr,idx - start)
        char_d[svar[idx]] = idx
    print(max_lenstr)



test_cases = int(input())
for idx in range(test_cases):
    svar = input()
    if svar =='':
        print(0)
    elif len(svar)==1:
        print(1)
    else:
        char_d = {}
        max_lenstr = 0
        start = -1
        # res =''
        for idx in range(len(svar)):
            if svar[idx] in char_d:
                # print(res)
                # print(char_d)
                # char_d[svar[idx]]+=1
                start = max(start,char_d[svar[idx]])
                # res=''
                # print(char_d)
            # res+=svar[idx]
            max_lenstr = max(max_lenstr,idx - start )
            char_d[svar[idx]] = idx
        print(max_lenstr)
            
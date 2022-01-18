def Grovlye(svar):
    if len(svar)==1:
        return svar
    k = len(svar)//2
    new_1 = ''.join(sorted(svar))
    # new_2 = ''.join(sorted(svar[k:]))
    res = new_1[:k:1] + new_1[-1] + new_1[-2:k-1:-1]
    # print(res)
    # Arr = list(res)
    # summ = 0
    # for idx in range(len(Arr)):
    #     distance = abs(idx-k)
    #     # print(distance, ord(Arr[idx]))
    #     summ+= distance * ord(Arr[idx])
    return res

test_cases = int(input())
for each in range(test_cases):
    svar = input()
    print(Grovlye(svar))



                                                                              #Approach2

def Grovlye(svar):
    if len(svar)==1:
        return svar

    svar_sorted = ''.join(sorted(svar))
    new_1 = ''
    new_2 = ''
    for idx in range(len(svar)):
        if idx%2 ==0:
            new_1+=svar_sorted[idx]
        else:
            new_2+=svar_sorted[idx]
    res = new_1 + new_2[::-1]
    return res

test_cases = int(input())
for each in range(test_cases):
    svar = input()
    print(Grovlye(svar))
from collections import Counter
size_arr = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
freq = Counter(arr)
# print(freq)
flag = True

for i in range(2,arr[-1]+1):
    if freq[i]>freq[i-1]:
        flag = False
        break

if flag == True:
    res=[]
    for i in range(arr[-1],0,-1):
        count = freq[i]
        curr =[]
        if count>0:
            for j in range(1,i+1):
                curr.append(j)
                freq[j]-=count
            # print(curr)
            for k in range(count):
                res.append(curr)
            # print(res)
    res.sort(key = lambda x:len(x))
    print(len(res))
    for each in res:
        print(*each)
else:
    add=0
    for i in range(arr[-1],1,-1):
        if freq[i]>freq[i-1]:
            temp=(freq[i] - freq[i-1])
            freq[i-1]+=temp
            add+=temp
            # print(temp, add, i)
    print(add)
from collections import defaultdict
def groupAnagrams(strs):
    Arr = list(strs)
    if len(Arr)==0:
        return [[""]]
    if len(Arr)==1:
        return [Arr]
    
    Arr.sort()
    d = defaultdict(list)
    for each in Arr:
        each_sorted = ''.join(sorted(each))
        # print(each_sorted)
        d[each_sorted].append(each)
        # print(d)
    
    res =[]
    for each in d.values():
        res.append(each)
    
    return res

if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        print(groupAnagrams(arr))
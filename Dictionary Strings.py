def maxstr(main_str,words):
    for each in words:
        j=0
        i=0
        while j<=len(main_str)-1:
            if each[i]==main_str[j]:
                i+=1
            j+=1
            if i==len(each):
                return each
    return ''

main_str = input()
word_dict = [x for x in input().split()]
word_dict.sort(key=lambda x:len(x),reverse=True)
print(len(maxstr(main_str,word_dict)))
def addStrings(num1, num2):     
    ### Here num1 & num2 are strings [Return the addition of these two strings as string]
    if len(num1)<=len(num2):
        list1 = list(num1)
        list2 = list(num2)
    else:
        list1 = list(num2)
        list2 = list(num1)
    carry = 0
    dig =''
    # print(list1)
    # print(list2)
    for i in range(1,len(list1)+1):
        val = int(list1[-i]) + int(list2[-i])+carry
        carry = val//10
        dig+=str(val%10)
    
    for i in range(len(list1)+1,len(list2)+1):
        val = int(list2[-i])+carry
        carry = val//10
        dig+=str(val%10)
    if carry!=0:
        dig+=str(carry)
    # print(dig)
    addstr = dig[::-1]
    return addstr

## Do not change anything below this line:

for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))
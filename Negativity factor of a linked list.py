# cook your dish here
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current
    
    # complete the function given below
    @staticmethod
    def Negativity(List):
        temp = List.head
        count = 0
        i = 0
        while (temp!=None):
            if temp.data<0:
                count+=1
            temp = temp.next
            i+=1
        return int((count/i)*100)

ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
# print(curr)
for i in num[1:]:
    curr = LL.insert_node(i, curr)
    # print(curr)
print(LL.Negativity(ll))
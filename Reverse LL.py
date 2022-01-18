class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
def reverse_llist(llist):
    # Implement this
    temp1,temp2 = llist.head,llist.head.next
    # temp2 = llist.head.next
    llist.head.next = None

    while temp2!=None:
        temp1,temp2 = temp2,temp2.next
        # temp2 = temp2.next
        temp1.next = llist.head
        llist.head = temp1
    
    return llist
 
a_llist = LinkedList()
n = int(input())
l = list(map(int, input().split(' ')))
# data_list = input('Please enter the elements in the linked list: ').split()
for data in l:
    a_llist.append(int(data))
 
reverse_llist(a_llist)
a_llist.display()
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
    
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
 
def length_llist(llist):
    length = 0
    current = llist.head
    while current:
        current = current.next
        length = length + 1
    return length
 
 
def return_n_from_last(llist, n):
   #Implement this
   lent = length_llist(llist)
   temp = llist.head
   i = 0
   while(i!=(lent-n)):
        temp = temp.next
        i+=1
   return temp.data
   
N, n = map(int, input().split(' ')) 
a_llist = LinkedList()

l = list(map(int, input().split(' ')))
for i in l:
    a_llist.append(i) 

value = return_n_from_last(a_llist, n)
a_llist.printList()
print(value)
# Node class 
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, key): 
        self.key = key 
        self.next = None

class LinkedList:
# Function to initialize head 
    def __init__(self): 
        self.head = None
        self.tail = None

    def insert(self, key):
        if not self.head:
            self.head = Node(key)
            self.tail = self.head

        else:
            self.tail.next = Node(key)
            self.tail = self.tail.next

# ------------ DO NOT MANE ANY CHANGE ABOVE THIS LINE ---------
    def search(self, key):
        # WRITE YOUR IMPLEMENTATION OF SEARCH HERE
        temp=self.head
        while temp!=None:
            if temp.key==key:
                return True
            temp = temp.next
        return False
        
# ----------- DO NOT MAKE ANY CHANGES BELOW THIS LINE ---------
# reading from input and making linked list
num_tests = int(input())

for test in range(0, num_tests):
    ll = LinkedList()
    key = int(input())
    elements = [int(e) for e in input().split(" ")]
    [ll.insert(e) for e in elements] 
    print(ll.search(key))
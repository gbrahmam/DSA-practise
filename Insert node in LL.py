class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
          
    def makeListAndPrint(self):
        #####WRITE CODE HERE####
        start=[]
        end=[]
        self.tail=self.head
        temp=self.tail
        while temp!=None and temp.next!=None:
            key,indicator = int(temp.data),int(temp.next.data)
            if indicator==0:
                start.append(key)
            elif indicator==1:
                end.append(key)
            temp=temp.next.next
        res = start[::-1] + end
        for each in res:
            print(each,end=' ')
        return

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    linkedList.makeListAndPrint()
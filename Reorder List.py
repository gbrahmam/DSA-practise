# Node class 
class Node: 
	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList:
# Function to initialize head 
    def __init__(self): 
        self.head = None

    def printList(self): 
        temp = self.head 
        while(temp!=None): 
            print(temp.data, end=" ")
            temp = temp.next
# Do not change anything above this line
                
    def reorderList(self):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        def reversal(hed):
            curr = hed
            prev = None
            while curr!=None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        length=0
        current = llist.head
        while current!=None:
            current = current.next
            length = length + 1

        val=llist.head
        for i in range(length//2):
            val = val.next

        last = reversal(val.next)
        val.next=None
        start = llist.head
        while last!=None:
            temp1 = start.next
            start.next = last
            temp2 = last.next
            last.next = temp1
            start=temp1
            last=temp2
        return llist.head

# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    llist.head = llist.reorderList()
    llist.printList()
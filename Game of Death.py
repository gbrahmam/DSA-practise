class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList:
# Function to initialize head 
    def __init__(self): 
        self.head = None
    
    def printList(self,l,curr): 
        temp = curr
        while(l!=0): 
            print (temp.data,end=' ') 
            temp = temp.next
            l-=1

def GameDeath(LL,n,k):
    curr = LL.head
    if n==1:
        return curr.data
    if k%n!=0:
        k = k%n
    else:
        k = n

    if k==1:      #serial kill
        l=1
        while l<n:
            curr = curr.next
            l+=1
        return curr.data
    l = n
    # llist.printList(l,curr)
    # print()
    while l!=1:
        skip =1
        while skip<(k-1):
            curr=curr.next
            skip+=1
        curr.next = curr.next.next
        curr=curr.next
        l-=1
        # llist.printList(l,curr)
        # print()
    return curr.data

for _ in range(int(input())):

    n,k = [int(x) for x in input().split()]

    # Start with the empty list 
    llist = LinkedList() 

    temp = [x for x in range(1,n+1)]

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

    link = 0
    if(link!=-1):
        t = llist.head
        for _ in range(link-1):
            t = t.next
        curr.next = t
    
    print(GameDeath(llist,n,k))



                                                                                   #Approach2---->100%

def deathgame(N,pos):
    if N==1:
        return 1
    return (deathgame(N-1,k)+k-1)%N+1

for tests in range(int(input())):
    n,k = [int(i) for i in input().split()]
    print(deathgame(n,k))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
linklist=LinkedList()
linklist.head=Node(1)
linklist.head.next=Node(4)
linklist.head.next.next=Node(6)
while linklist.head != None:
    print(linklist.head.data,end=" ")
    linklist.head=linklist.head.next








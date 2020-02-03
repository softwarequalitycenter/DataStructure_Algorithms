class Node :
    def __init__(self, d):
        self.next = None
        self.data = d

class LinkedList :
    def __init__(self) :
        self.head = None

    def add(self,d):
        if self.head == None:
            self.head = Node(d)
            return
        else:
            ptr = self.head
            while (ptr.next):
                ptr = ptr.next
            ptr.next = Node(d)

    def printList(self):
        if self.head == None:
            print ("none")
        else:
            ptr = self.head
            while (ptr):
                print (ptr.data)
                ptr=ptr.next

    def reverseList(self):
        prev = None
        cur = self.head
        while (cur is not None) :
             temp = cur.next
             cur.next = prev
             prev = cur
             cur = temp
        self.head=prev


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.printList()

l.reverseList()
l.printList()



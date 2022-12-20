class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class linkedlist:
    def __init__(self):
        self.head = None
    def pus(self,data):
        n = node(data)
        n.next = self.head
        self.head = n
    def printl(self):
        while self.head!=None:
            print(self.head.data)
            self.head = self.head.next
    def rot(self,n):
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = self.head
        self.head.prev = curr
        curr = self.head
        curr2 = self.head.next
        c = 1
        while c<n:
            curr = curr.next
            curr2 = curr2.next
            c+=1
        t = curr2
        curr.next = None
   
        t.prev = None
        self.head = curr2
l = linkedlist()
l.pus(6)
l.pus(5)
l.pus(4)
l.pus(3)
l.pus(2)
l.pus(1)
n = 2
l.rot(n)
l.printl()


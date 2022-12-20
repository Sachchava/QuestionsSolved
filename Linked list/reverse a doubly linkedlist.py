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
    def rot(self):
        t = None
        head = curr = self.head
        while curr!=None:
            t = curr.prev
            curr.prev = curr.next
            curr.next = t
            curr = curr.prev
        if t !=None:
            head = t.prev
        return head
    def printk(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next
l = linkedlist()
l.pus(5)
l.pus(4)
l.pus(3)
l.pus(2)
l.pus(1)
l.rot()
l.printk()


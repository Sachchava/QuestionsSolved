class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def pus(self,d):
        n = node(d)
        n.next = self.head
        self.head = n
    def printl(self):
        r = self.head
        while(r):
            print(r.data)
            r = r.next
    def rd(self):
        # p1 = self.head
        # p2 = self.head
        # while(p1!=None):
        #     while(p2.next!=None):
        #         if p1.data==p2.next.data:
        #             p2.next = p2.next.next
        #         else:
        #             p2 = p2.next
        #     p1 = p1.next
        a = set()
        p = self.head
        a.add(p.data)
        while(p.next!=None):
            if p.next.data  in a:
                p = p.next
            else:
                a.add(p.next.data)
        return a

l = linkedlist()
l.pus(1)
l.pus(4)
l.pus(4)
l.pus(3)
l.pus(4)
l.pus(3)
l.pus(4)
l.pus(3)
l.pus(2)
l.pus(4)
print(l.rd())
# l.printl()



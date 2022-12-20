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
        t = self.head
        while(t):
            print(t.data)
            t = t.next
    def ll(self):
        c = self.head
        v  = 0
        while(c):
            v+=1
            c = c.next
        t = int(v/2)
        b =self.head
        for i in range(t):
            b = b.next
        print(b.data)
        
    def m(self):
        s = self.head 
        f = self.head
        while( f != None and f.next!=None):
            s = s.next
            f = f.next.next
        return s.data



l = linkedlist()
l.pus(6)
l.pus(5)
l.pus(4)
l.pus(3)
l.pus(2)
l.pus(1)
l.ll()
# l.printl()
print(l.m())


class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def append(self,d):
        n = node(d)
        if self.head is None:
            self.head = n
            return
        l = self.head 
        while(l.next):
            l = l.next
        l.next = n
    def re(self):
        p = self.head
        while(p!=None):
            if p.data==p.next.data:
                p.next = p.next.next
            p = p.next
    def printl(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next
l = linkedlist()
l.append(1)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(4)
l.re()
l.printl()

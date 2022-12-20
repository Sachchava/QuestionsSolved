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
    def ltf(self):
        sl = self.head
        l = self.head.next
        while(l.next!=None):
            l = l.next
            sl = sl.next
        t = sl.next
        sl.next = None
        t.next = self.head
        self.head = t
        
       
 
        
l = linkedlist()
l.pus(4)
l.pus(3)
l.pus(2)
l.pus(1)
l.ltf()
l.printl()
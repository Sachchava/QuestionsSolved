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
    def ll(self,n):
        c = self.head
        v  = 0
        while(c):
            v+=1
            c = c.next
        
        t = v-n
        
        b =self.head
        for i in range(t):
            b = b.next
        print(b.data)
l = linkedlist()
l.pus(4)
l.pus(3)
l.pus(2)
l.pus(1)
n = 3
l.ll(n)
# l.printl()


class node():
    def __init__(self,data):
        self.data= data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def append(self,n):
        nn = node(n)
        if self.head is None:
            self.head = nn
            return
        l = self.head
        while(l.next):
            l = l.next
        l.next = nn
    def printl(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next
    def de(self):
        curr = self.head
        while(curr!=None):
            next = curr.next
            del curr
            curr = next
        self.head = None
l = linkedlist()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
# l.printl()
l.de()
l.printl()


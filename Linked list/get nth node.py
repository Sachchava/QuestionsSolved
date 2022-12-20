class node():
    def __init__(self,data):
        self.data= data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def append(self,dat):
        m = node(dat)
        if self.head is None:
            self.head = m
            return
        l = self.head
        while(l.next):
            l = l.next
        l.next = m
    def printl(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next
    def f(self,n):
        c = self.head
        for i in range(n):
            c = c.next
        return c.data
l = linkedlist()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
n = 3
l.printl()
print(l.f(n))

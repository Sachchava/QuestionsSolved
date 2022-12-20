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
    def s(self,k):
        c = self.head
        while(c!=None):
            if c.data==k:
                return True
            c=c.next
        return False
    def ll(self):
        p = self.head
        c = 0
        while(p!=None):
            c+=1
            p = p.next
        return c
    def rc(self):
        t = self.head
        if (t is None):
            return 0
        else:
            return 1 + self.rc() 
l = linkedlist()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.printl()
print(l.ll())

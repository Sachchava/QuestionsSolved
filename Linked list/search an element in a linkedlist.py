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
    def rs(self,li,k):
        if (not li):
            return 0
        if (li.data==k):
            return True
        return self.rs(li.next,k)
l = linkedlist()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

print(l.s(1))
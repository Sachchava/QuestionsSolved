class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def push(self,d):
        n = node(d)
        n.next = self.head
        self.head = n
    def ll(self,n):
        c = self.head
        p = 0
        while(c!=None):
            if c.data ==n:
                p+=1
            c = c.next
        return p
l = linkedlist()
l.push(4)
# l.push(1)
# l.push(4)
# l.push(1)
# l.push(1)
# l.push(1)
n = 4
print(l.ll(n))

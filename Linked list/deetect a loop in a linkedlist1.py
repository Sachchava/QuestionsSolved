class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def append(self,d):
        n = node(d)
        if self.head == None:
            self.head = n
            return
        l = self.head
        while(l.next):
            l= l.next
        l.next = n
    def dloop(self):
        slow = self.head
        fast = self.head 
        while(fast!= None and slow!=None  and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            c = 1
            if fast == slow:
                slow = slow.next 
                while fast!=slow:
                    c+=1
                return c
    # def dloop1(self):

l = linkedlist()
l.append(1)
l.append(2)
l.append(15)
l.append(14)
l.append(12)
l.append(3)

print(l.dloop())

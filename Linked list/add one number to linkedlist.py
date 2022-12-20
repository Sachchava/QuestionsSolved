class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def pus(self,data):
        n = node(data)
        n.next = self.head
        self.head  = n
    def printl(self):
        t= self.head
        while(t):
            print(t.data)
            t = t.next
    def r(self):
        curr = self.head
        prev = None
        
        while(curr!=None):
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next   
            self.head = prev
    def aa(self):
        self.head = self.r()
        curr = self.head
        while(curr!=None):
            if curr.data == 9 and curr.next == None:
                n = node(0)
                curr.data = 1
                n.next = self.head
                self.head = n
                curr = curr.next
            elif curr.data ==9:
                curr.data = 0
                curr= curr.next
            else:
                curr.data = curr.data + 1
                curr = curr.next
                break
        self.head = self.r()
        return self.head



l = linkedlist()
l.pus(1)
l.pus(9)
l.pus(9)
l.pus(1)
l.printl()
l.aa()
l.printl()
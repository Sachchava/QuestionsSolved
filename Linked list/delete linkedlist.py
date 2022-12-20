class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def append(self,newdata):
        new = node(newdata)
        if self.head is None:
            self.head = new
            return
        t = self.head
        while(t.next):
            t = t.next
        t.next = new
    def deletel(self,k):
        temp = self.head
        if self.head == None:
            return
        if (temp is not None):
            if (temp.data == k):
                self.head = temp.next
                temp = None
                return 
        while(temp.next.data!=k):
            temp = temp.next
        todelete = temp.next
        temp.next = temp.next.next
        todelete = None
    def printl(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next
l = linkedlist()
l.append(2)
l.append(1)

l.append(3)
l.append(4)

l.deletel(2)
l.printl()

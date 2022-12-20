class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def push(self,newdata):
        newnode = node(newdata)
        newnode.next = self.head
        self.head = newnode
    def printl(self):
        t = self.head 
        while(t):
            print(t.data)
            t = t.next
    def detect(self):
        if self.head is None :
            return False
        slow = self.head
        fast = self.head
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
ll = linkedlist()
ll.push(1)
ll.push(3)
ll.push(4)

if ll.detect():
    print("Loop present")
else:
    print("loop absent")

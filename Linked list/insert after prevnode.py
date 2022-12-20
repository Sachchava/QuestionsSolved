class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,newdata):
        newnode = node(newdata)
        newnode.next = self.head
        self.head = newnode
    def insertafter(self,prev,newdata):
        if prev is None:
            return
        newnode = node(newdata)
        newnode.next = prev.next
        prev.next = newnode
    def append(self,newadata):
        newnode = node(newadata)
        if self.head is None:
            self.head = newnode
            return
        last = self.head 
        while(last.next):
            last = last.next
        last.next = newnode
    def printl(self):
        t = self.head
        while(t): 
            print(t.data)
            t = t.next
if __name__ == '__main__':
    ll = linkedlist()
    ll.append(4)
    ll.append(5)
    ll.push(1)
    ll.insertafter(ll.head,2)
    ll.printl()
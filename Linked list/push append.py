class node:
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
    def append(self,newdata):
        newnode = node(newdata)        
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newnode
    def printlist(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next
if __name__ == '__main__':
    ll = linkedlist()
    ll.append(5)
    ll.append(6)
    ll.push(3)
    ll.printlist()
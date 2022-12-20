class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def append(self,newdata):
        newnode = node(newdata)
        if self.head is None:
            self.head = newnode
            return
        last = self.head 
        while(last.next):
            last = last.next
        last.next = newnode
    def reversee(self,head):
        if head is None or head.next is None:
            return head
        r = self.reversee(head.next)
        head.next.next = head
        head.next = None
        return r
    def printl(self):
        temp = self.head
        while(temp): 
            print(temp.data)
            temp = temp.next
if __name__ =='__main__':
    ll = linkedlist()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.printl()
    ll.head = ll.reversee(ll.head)
    ll.printl()
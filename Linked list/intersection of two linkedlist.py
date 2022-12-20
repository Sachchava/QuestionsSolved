class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def append(self,data):
        n = node(data)
        if self.head is None:
            self.head = n
            return
        l = self.head
        while(l.next):
            l = l.next
        l.next = n
    def printl(self):
        r = self.head
        while(r):
            print(r.data)
            r = r.next
class sol():
    def i(l1,l2):
        p1 = l1
        p2 = l2
        curr = None
        head = None
        while(p1 != None and p2 != None):
            if p1.data == p2.data:
                if head ==None:
                    n = node(p1.data)
                    head = n
                    curr = n
                else:
                    n = node(p1.data)
                    curr.next = n
                    curr = curr.next
                p1 = p1.next
                p2 = p2.next   
            else:
                if p1.data < p2.data:
                    p1 = p1.next
                else:
                    p2 = p2.next
        return head

def printl(self):
    r = self.head
    while(r):
        print(r.data)
        r = r.next
if __name__== '__main__':
    l1 = linkedlist()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    # l1.printl()
    l2 = linkedlist()
    l2.append(3)
    l2.append(5)
    # l2.printl()
    l3 = linkedlist()
    res = i(l1.head,l2.head)
    printl(res)
    print()


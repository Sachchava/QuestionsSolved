class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def pus(h,data):
    n = node(data)
    n.next = h
    h = n
def printl(self):
    t = self.head
    while t:
        print(t.data)
        t = t.next

def pus (head1,x):
    start = head1
    end = head1
    while end.next!=None:
        end = end.next
    print(end.data)
    while start!=end and end.prev!=start:
        if start.data + end.data==x:
            print(start.data,end.data)
            start = start.next
            end = end.prev
        else:
            if start.data + end.data > x:
                end = end.prev
            else: 
                start = start.next


h = None
h = pus(h,1)
h = pus(h,2)
h = pus(h,3)
h = pus(h,4)
h = pus(h,5)
h = pus(h,6)
x = 5
print(h)
pus(h,x)
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,data):
        n = node(data)
        n.next = self.head
        self.head = n
    def printk(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next
    # def co(self,head,x):
    #     c = 0
    #     first = head
    #     while first!=None:
    #         second = first.next
    #         third = head
    #         while third.next!= None:
    #             third = third.next
    #         p = x - first.data
    #         while second!=third and third.next != second:
    #             if second.data+third.data == p:
    #                 c+=1
    #                 second = second.next
    #                 third = third.prev
    #             else:
    #                 if second.data+third.data > p:
    #                     second = second.next
    #                 else:
    #                     third= third.prev
    #         first = first.next
    #     return c
    def end(self):
        curr = self.head
        c = 0
        while curr.next!=None:
            curr = curr.next
            c+=1
        new = self.head
        print(c)
        
        while c!=3:
            new = new.next
            c-=1
        return curr.data,new.data
l = linkedlist()
l.push(7)
l.push(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
x = 4
l.printk()
print(l.end())
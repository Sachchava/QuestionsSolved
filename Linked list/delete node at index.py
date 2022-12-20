from typing import TextIO


class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def pus(self,a):
        n = node(a)
        n.next = self.head 
        self.head = n
    def printl(self):
        t = self.head
        while(t):
            print(t.data)
            t =t.next
    def datind(self,pos):
        if self.head == None:
            return
        t = self.head
        if t != None:
            if t.next == None:
                if pos==0:
                    self.head = t.next
                    t = None
                    return
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        tod = temp.next
        temp.next = temp.next.next
        tod = None
l = linkedlist()
l.pus(4)
l.pus(3)

l.pus(2)
l.pus(1)

l.datind(3)
l.printl()


        
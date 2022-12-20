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
        self.head =  newnode
    def printl(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp =temp.next
    def reversel(self):
        prev = None
        current = self.head
        while(current!=None):
            next = current.next
            current.next = prev

            prev = current
            current = next
        self.head = prev
if __name__ == '__main__':
    ll = linkedlist() 
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
   
 
    ll.printl()
    ll.reversel()
    ll.printl()
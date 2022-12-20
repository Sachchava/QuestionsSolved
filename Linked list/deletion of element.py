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
    def deletel(self,val):
        temp = self.head
        while(temp.next.data !=val):
            temp = temp.next
        todelete = temp.next
        temp.next = temp.next.next
        todelete = None
    # def deletel(self,key):
    #     temp = self.head
    #      # If head node itself holds the key to be deleted
    #     if (temp is not None):
    #         if (temp.data == key):
    #             self.head = temp.next
    #             temp = None
    #             return
    #             # Search for the key to be deleted, keep track of the
    #     # previous node as we need to change 'prev.next'
    #     while(temp is not None):
    #         if (temp.data == key):
    #             break
    #         prev = temp 
    #         temp = temp.next
    #        # if key was not present in linked list
    #     if (temp ==None):
    #         return
        
    #     # Unlink the node from linked list
    #     prev.next = temp.next
    #     temp = None
    def printl(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
if __name__ == '__main__':
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.deletel(2)
    ll.printl()

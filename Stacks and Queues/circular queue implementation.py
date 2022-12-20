class circularqueue:
    def __init__(self,k):
        self.maxsize = k
        self.data = [0]*k
        self.head = 0
        self.tail = -1
    def isempty(self):
        if self.tail==-1:
            return False
        return True
    def isfull(self):
        if not self.isempty() and (self.tail+1)%self.maxsize==self.head:
            return True
        return False
    def front(self):
        if self.isempty():
            return -1
        else:
            return self.data[self.head]
    def rear(self):
        if self.isempty():
            return -1
        else:
            return self.data[self.tail]
    def enqueue(self,val):
        if self.isfull():
            return False
        self.tail = (self.tail+1)%self.maxsize
        self.data[self.tail] = val
    def dequeue(self):
        if self.isempty():
            return False
        if self.head == self.tail:
            self.head,self.tail = 0,-1
        else:
            self.head = (self.head+1)%self.maxsize
        return True
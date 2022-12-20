from queue import Queue
class solution:
    def __init__(self):
        self.q1 = Queue(maxsize=3)
        self.q2 = Queue(maxsize=3)
    def push(self,el):
        self.q1.put(el)
        while self.q1 !=[]:
            self.q2.put(self.q1.get())
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
    def popq(self):
        self.q2.get_nowait()
    def topq(self):
        print(self.q2[0])
    def printq(self):
        print(self.q2)
if __name__ == '__main__':
    s = solution()
    s.push(1)
    s.push(2)
    s.push(3)
    s.popq()
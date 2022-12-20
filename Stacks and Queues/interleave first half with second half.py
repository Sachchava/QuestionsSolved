from queue import Queue
class solution:
    def interleave(self,q):
        stack = []
        length = int(q.qsize()/2)
        for i in range(length):
            stack.append(q.queue[0])
            q.get()
        while stack!=[]:
            q.put(stack.pop(0))
            q.put(q.queue[0])
            q.get()


if __name__ == "__main__":
    q = Queue()
    q.put(11) 
    q.put(12) 
    q.put(13) 
    q.put(14) 
    q.put(15) 
    q.put(16) 
    q.put(17) 
    q.put(18) 
    q.put(19) 
    q.put(20) 
    (solution().interleave(q))
    for i in range(q.qsize()):
        print(q.get())
        
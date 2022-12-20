from queue import Queue
class solution:
    def reverse(self,q,k):
        n = q.qsize()
        length = n-k
        self.reversek(q,k)
        while length!=0:
            q.put(q.queue[0])
            q.get()
            length-=1
        return q
    def reversek(self,q,k):
        if k == 0:
            return 
        data = q.queue[0]
        q.get()
        k-=1
        self.reversek(q,k)
        q.put(data)
        return q
if __name__ == "__main__":
    Queue = Queue()
    Queue.put(10)
    Queue.put(20)
    Queue.put(30)
    Queue.put(40)
    Queue.put(50)
    Queue.put(60)
    Queue.put(70)
    Queue.put(80)
    Queue.put(90)
    Queue.put(100)

    for i in range(Queue.qsize()):
        print(Queue.queue[0])
        Queue.get()
    Queue.put(10)
    Queue.put(20)
    Queue.put(30)
    Queue.put(40)
    Queue.put(50)
    Queue.put(60)
    Queue.put(70)
    Queue.put(80)
    Queue.put(90)
    Queue.put(100)
    k = 5
    print("=======")
    (solution().reverse(Queue,k))
    for i in range(Queue.qsize()):
        print(Queue.queue[0])
        Queue.get()
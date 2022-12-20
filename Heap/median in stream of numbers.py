from heapq import heappush,heappop,_heappop_max
class solution:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
    def getmin(self,q):
        return q[0]
    def getmax(self,q):
        return q[-1]
    def insert(self,n):
        if self.maxheap ==[] or self.getmin(self.maxheap)>=n:
            heappush(self.maxheap,n)
        else:
            heappush(self.minheap,n)
        if len(self.maxheap)<len(self.minheap):
            m = heappop(self.minheap)
            heappush(self.maxheap,m)
        elif len(self.maxheap) >len(self.minheap)+1:
            n = _heappop_max(self.maxheap)
            heappush(self.minheap,n)
    def getmedian(self):
        med = 0
        if len(self.maxheap)==len(self.minheap):
            # print(self.getmin(self.minheap))
            # print(self.getmax(self.maxheap))
            med = self.getmin(self.minheap)+self.getmax(self.maxheap)
            med = med/2
        elif len(self.maxheap)>len(self.minheap):
            med = self.getmax(self.maxheap)
        print(med)
if __name__ == "__main__":
    s = solution()
    s.insert(5)
    print(s.maxheap,s.minheap)
    s.getmedian()
    s.insert(15)
    print(s.maxheap,s.minheap)
    s.getmedian()
    s.insert(10)
    print(s.maxheap,s.minheap)
    s.getmedian()
    s.insert(20)
    print(s.maxheap,s.minheap)
    s.getmedian()
    s.insert(3)
    print(s.maxheap,s.minheap)
    s.getmedian()

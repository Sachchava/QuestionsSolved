from heapq import heapify,heappush,heappop
class heapss:
    def __init__(self):
        self.heap = []
    def getMin(self):
        return self.heap[0]
    def extractMin(self):
        return heappop(self.heap)
    def insertKey(self,k):
        heappush(self.heap,k)
    def parent(self,i):
        return int(i-1/2)
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()
if __name__ == "__main__":
    heapObj = heapss()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    # heapObj.deleteKey(1)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)#'''for inserting one by one timecomplexity is nlog(n) and if array is used heapifying that array has only n time complexity'''
    heapObj.insertKey(45)
    print(heapObj.extractMin())
    print(heapObj.extractMin())
    print(heapObj.extractMin())
    print(heapObj.extractMin())
    print(heapObj.extractMin())
    # print(heapObj.getMin())
    # heapObj.decreaseKey(2, 1)
    # print(heapObj.getMin())
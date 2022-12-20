import heapq as hq
class solution:
    def buildheap(self,arr):    
        start = int((len(arr)/2))
        for i in range(start,-1,-1):
            self.maxheapify(arr,i,len(arr))

    def buildheap1(self,arr):    
        start = int(len(arr)/2)
        for i in range(start,-1,-1):
            self.minheapify(arr,i,len(arr))
            

    def maxheapify(self,arr,i,n):
        largest = i
        left = (2*i)+1
        right = (2*i)+2
        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.maxheapify(arr,largest,n)
    def minheapify(self,arr,i,n):
        smallest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[left]<arr[smallest]:
            smallest = left
        if right<n and arr[right]<arr[smallest]:
            smallest = right
        if smallest!=i :
            arr[smallest],arr[i] = arr[i],arr[smallest]
            self.minheapify(arr,smallest,n)
    def printheap(self,arr):
        print()
        for i in range(len(arr)):
            print(arr[i],end = " ")
if __name__ == "__main__":
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    solution().buildheap(arr)
    solution().printheap(arr)
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    solution().buildheap1(arr)
    solution().printheap(arr)

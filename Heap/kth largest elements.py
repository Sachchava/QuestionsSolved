class solution:
    def buildkthmax(self,arr):
        start = int((len(arr)/2))
        for i in range(start,-1,-1):
            self.maxheap(arr,i,len(arr))
        for i in range(len(arr)-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.maxheap(arr,0,i)
    def maxheap(self,arr,i,n):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right
        if largest!=i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.maxheap(arr,largest,n)
    def printheap(self,arr,k):
        for i in range(len(arr)):
            print(arr[i],end = ' ')
if __name__ == "__main__":
    arr = [1,23,12,9,30,2,50]
    k = 3
    solution().buildkthmax(arr)
    (solution().printheap(arr,k))
class solution:
    def heapsortt(self,arr):
        start = int((len(arr)/2))
        for i in range(start,-1,-1):#O(n)time
            self.minheapify(arr,i,len(arr))
        # for i in range(len(arr)-1,0,-1):#O(nlog(n))time to replace and heapify
        #     arr[0],arr[i] = arr[i],arr[0]
        #     self.heapify(arr,0,i)
    def heapify(self,arr,i,n):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right
        if largest != i:
            arr[largest],arr[i] = arr[i],arr[largest]
            self.heapify(arr,largest,n)
    def minheapify(self,arr,i,n):
        smallest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[left]<arr[smallest]:
            smallest = left
        if right<n and arr[right]<arr[smallest]:
            smallest = right
        if smallest != i:
            arr[smallest],arr[i] = arr[i],arr[smallest]
            self.heapify(arr,smallest,n)
    def printheap(self,arr):
        for i in range(len(arr)):
            print(arr[i],end = ' ')
if __name__ == "__main__":
    arr = [1,23,12,9,30,2,50]
    solution().heapsortt(arr)
    solution().printheap(arr)
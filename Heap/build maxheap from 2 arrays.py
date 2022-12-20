class solution:
    def heapsortt(self,arr):
        start = int((len(arr)/2))
        for i in range(start,-1,-1):
            self.heapify(arr,i,len(arr))
        for i in range(len(arr)-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,0,i)
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
    def printheap(self,arr):
        for i in range(len(arr)):
            print(arr[i],end = ' ')
if __name__ == "__main__":
    arr1 = [10, 5, 6, 2]
    arr2 = [12, 7, 9]
    arr = arr1 + arr2
    print(arr)
    solution().heapsortt(arr)
    solution().printheap(arr)
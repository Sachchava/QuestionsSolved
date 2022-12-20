class solution:
    def minheaptomaxheap(self,arr):
        start = int(len(arr)/2)
        for i in range(start,-1,-1):
            self.maxheap(arr,i,len(arr))
    def maxheap(self,arr,i,n):
        large = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[left]>arr[large]:
            large = left
        if right<n and arr[right]>arr[large]:
            large = right
        if large!=i:
            arr[large],arr[i] = arr[i],arr[large]
            self.maxheap(arr,large,n)
    def printh(self,arr):
        for i in range(len(arr)):
            print(arr[i],end = " ")

if __name__ =="__main__":
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]    
    solution().minheaptomaxheap(arr)
    solution().printh(arr)
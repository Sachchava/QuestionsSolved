class solution:
    def rdis(self,arr,i):
        if i == len(arr):
            return 
        self.rdis(arr,i+1)
        print(arr[i])
if __name__ == "__main__":
    arr = [10,20,30,40,50]
    i = 0
    solution().rdis(arr,i)
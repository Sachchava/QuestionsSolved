class solution:
    def dis(self,arr,i):
        if i == len(arr):
            return 
        print(arr[i])
        self.dis(arr,i+1)
if __name__ =="__main__":
    arr = [10,20,30,40,50]
    i = 0
    solution().dis(arr,i)
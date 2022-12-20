class solution:
    def findx(self,arr,i):
        if i == len(arr):
            return -1
        if arr[i]==3:
            return i
        return self.findx(arr,i+1)
if __name__ == "__main__":
    arr = [2,5,6,2,7,6,4,5]
    print(solution().findx(arr,0))
class solution:
    def maxf(self,arr,i):
        if i ==len(arr)-1:
            return arr[i]
        m = self.maxf(arr,i+1)
        if m>arr[i]:
            return m
        else:
            return arr[i]
if __name__ == "__main__":
    arr = [312,4,2,3,234,12,111143,12341]
    print(solution().maxf(arr,0))
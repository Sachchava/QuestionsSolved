class solution:
    def mincandies(self,arr,k):
        arr = sorted(arr)
        free = k
        res = 0
        while arr !=[]:
            res+=arr[0]
            arr.pop(0)
            while k!=0:
                if arr!=[]:
                    arr.pop()
                    k-=1
                else:
                    return res
            k = free
        return res
    def maxcandies(self,arr,k):
        arr = sorted(arr)
        free = k
        res = 0
        while arr !=[]:
            res+=arr[-1]
            arr.pop()
            while k!=0:
                if arr!=[]:
                    arr.pop(0)
                    k-=1
                else:
                    return res
            k = free
        return res
    def mai(self,arr,k):
        return self.mincandies(arr,k),self.maxcandies(arr,k)
        
if __name__ == "__main__":
    arr = [3, 2,5, 1,4]
    k = 4
    print(solution().mai(arr,k))
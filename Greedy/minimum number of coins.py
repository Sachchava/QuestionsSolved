class solution:
    def findcoin(self,arr,v,res):
        while True:
            for i in range(len(arr)-1,-1,-1):
                if arr[i]<=v:
                    v-=arr[i]
                    res.append(arr[i])
                    break
                if v==0:
                    return res
                


if __name__ == "__main__":
    arr = [1,2,5]
    v = 11
    res = []
    print(solution().findcoin(arr,v,res))
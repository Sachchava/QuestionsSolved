class solution:
    def maxprofit(self,arr):
        maxxp = 0
        minn = arr[0]
        dpl = []
        for i in range(len(arr)):
            if arr[i]<=minn:
                minn = arr[i]
            profit = arr[i]-minn
            maxxp = max(profit,maxxp)
            dpl.append(maxxp)
        maxxp = 0
        maxx = arr[len(arr)-1]
        dpr = [0]*(len(arr))
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>maxx:
                maxx = arr[i]
            profit = maxx-arr[i]
            if profit>dpr[i+1]:
                dpr[i] = profit
            else:
                dpr[i] = dpr[i+1]
        maxsum = 0
        
        for i in range(len(arr)):
            maxsum = max(maxsum,dpl[i]+dpr[i])
        return dpl,dpr,maxsum
    def maxprofit1(self,arr):
        maxxp = 0
        minn = arr[0]
        top2 = set()
        for i in range(len(arr)):
            if arr[i]<minn:
                minn = arr[i]
                maxxp = 0
            profit = arr[i]-minn
            maxxp = max(maxxp,profit)
            top2.add(maxxp)
        sorted(top2)
        return top2

if __name__ == "__main__":
    arr = [11,6,7,19,4,1,6,18,4]
    # print(solution().maxprofit(arr))
    print(solution().maxprofit1(arr))
    print(arr)
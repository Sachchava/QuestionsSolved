class solution:
    def maxprofit(self,arr):
        minn = arr[0]
        maxxp = 0
        for i in range(len(arr)):
            if arr[i]<=minn:
                minn = arr[i]
            profit = arr[i]-minn
            maxxp = max(profit,maxxp)
        return maxxp
if __name__ == "__main__":
    arr =[11,6,7,19,4,1,6,18,4]
    print(solution().maxprofit(arr))
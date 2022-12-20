class solution:
    def minmoves(self,n,arr,dp):
        dp[n] = 0
        for i in range(n-1,-1,-1):
            if arr[i]>0:
                j = 1
                minn = float("inf")
                while j<=arr[i] and i+j<len(dp):
                    if dp[i+j]!=0:
                        minn = min(minn,dp[i+j])
                        j+=1
                if minn!=float("inf"):
                    dp[i] = minn+1
        return dp
if __name__ == "__main__":
    n = 10
    arr = [3,3,0,2,1,2,4,2,0,0]
    dp = [0]*(n+1)
    print(solution().minmoves(n,arr,dp))
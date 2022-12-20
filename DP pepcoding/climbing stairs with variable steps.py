class solution:
    def varpaths(self,n,dp,arr):
        dp[n]=1
        for i in range(n-1,-1,-1):
            j = 1
            while j<=arr[i] and i+j<len(dp):
                dp[i] += dp[i+j]
                j+=1
        return dp[0]

if __name__ == "__main__":
    n = 10
    dp = [0]*(n+1)
    arr = [3,3,0,2,1,2,4,2,0,0]
    print(solution().varpaths(n,dp,arr))
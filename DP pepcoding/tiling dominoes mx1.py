class solution:
    def tiling(self,n,m):
        dp = [0]*(n+1)
        for i in range(1,n+1):
            if i<m:
                dp[i] = 1
            elif i==m:
                dp[i] = 2
            else:
                dp[i] = dp[i-1]+dp[i-m]
        return dp[n]
if __name__ == "__main__":
    print(solution().tiling(39,16))
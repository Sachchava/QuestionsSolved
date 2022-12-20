class solution:
    def paintfence(self,n,k):
        dp = [0]*(n+1)
        mod = 100000007
        dp[1] = k
        dp[2] = k*k
        for i in range(3,n+1):
            dp[i] = ((k-1)*(dp[i-1]+dp[i-2]))%mod
        return dp[n]
if __name__ == "__main__":
    print(solution().paintfence(3,2))
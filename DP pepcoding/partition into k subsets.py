class solution:
    def partition(self,n,k,dp):
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if i==1 or i==j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (i*dp[i][j-1])+dp[i-1][j-1]
        return dp
if __name__ == "__main__":
    n = 5
    k = 2
    dp = [[0 for j in range(n+1)]for i in range(k+1)]
    print(dp)
    print(solution().partition(n,k,dp))
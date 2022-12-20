class solution:
    def pairs(self,n):
        dp = [0]*(n+1)
        
        for i in range(n+1):
            if i<=2:
                dp[i] = i
            else:
                dp[i] = dp[i-1]+dp[i-2]*(i-1)
        return dp[n]
if __name__ =="__main__":
    print    (solution().pairs(3))
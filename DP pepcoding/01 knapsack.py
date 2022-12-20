class solution:
    def knapsack(self,dp,wt,vl,cap):
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j>=wt[i-1]:
                    dp[i][j] = max(vl[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(wt)][cap]
    # def knapsack1(self,wt,vl,arr,ans,cap):

    #     self.knapsack1(wt[1:],vl[1:],arr,ans+vl[0],cap-wt[0])
if __name__ == "__main__":
    wt = [10, 20, 30]
    vl = [60, 100, 120]
    cap = 50
    dp = [[0 for j in range(cap+1)]for i in range(len(wt)+1)]
    print(solution().knapsack(dp,wt,vl,cap))
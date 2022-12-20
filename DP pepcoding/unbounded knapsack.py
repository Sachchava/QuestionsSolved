class solution:
    def unbounded(self,dp,wt,vl,cap):
        dp[0] = 0
        for i in range(1,len(dp)):
            maxx = 0
            for j in range(len(wt)):
                if i>=wt[j]:
                    maxx = max(maxx,dp[i-wt[j]]+vl[j])
            dp[i] = maxx
        return dp
if __name__ == "__main__":
    cap = 50
    wt = [10, 40, 20, 30]
    vl = [60, 40, 100, 120]
    dp = [0]*(cap+1)
    print(solution().unbounded(dp,wt,vl,cap))
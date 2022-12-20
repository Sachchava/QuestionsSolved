class solution:
    def maxprofit(self,arr,t,dp):
        n = len(arr)
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                maxx = dp[i][j-1]
                for k in range(1,j):
                    pttm1 = dp[i-1][k]
                    pttj = arr[j]-arr[k]
                    if pttm1+pttj>maxx:
                        maxx = pttm1 + pttj 
                dp[i][j] = maxx
        print(t,n-1)
        return dp[t][n-1]
if __name__ =="__main__":
    arr = [9,6,7,6,3,8]
    k = 1
    dp = [[0 for j in range(len(arr))]for i in range(k+1)]
    
    print(solution().maxprofit(arr,k,dp))

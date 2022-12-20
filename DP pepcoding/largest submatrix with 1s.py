class solution:
    def sizeof1s(self,arr):
        dp = [[-1 for j in range(len(arr[0]))]for i in range(len(arr))]
        ans = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if i == 0 or j == 0 or i == 0 and j == 0 or arr[i][j] == 0:
                    dp[i][j] = arr[i][j]
                else:
                    minn = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    dp[i][j] = minn+1
                    if dp[i][j]>ans:
                        ans = dp[i][j]
        return dp,ans   
                
if __name__ =="__main__":
    arr = [[0,1,0,1,0,1],
            [1,0,1,0,1,0],
            [0,1,1,1,1,0],
            [0,0,1,1,1,0],
            [1,1,1,1,1,1]]
    print(solution().sizeof1s(arr)) 
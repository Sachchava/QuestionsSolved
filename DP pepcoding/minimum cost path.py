class solution:
    def minimumcost(self,row,col,dp,arr):
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if i == row-1 and j == col-1:
                    dp[i][j] = arr[i][j]
                elif i == row-1:
                    dp[i][j] = dp[i][j+1]+arr[i][j]
                elif j == col-1:
                    dp[i][j] = dp[i+1][j] +arr[i][j]
                else:
                    dp[i][j] = min(dp[i][j+1],dp[i+1][j])+arr[i][j]
        return dp
if __name__ == "__main__":
    arr = [[0,1,4,2,8,2],[4,3,6,5,0,4],[1,2,4,1,4,6],[2,0,7,3,2,2],[3,1,5,9,2,4],[2,7,0,8,5,1]]
    row = len(arr)
    col = len(arr[0])
    dp = [[None for j in range(col)]for i in range(row)]
    print(arr)
    print(solution().minimumcost(row,col,dp,arr))
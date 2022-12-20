class solution:
    def path(self,dp,arr,row,col):
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if j == col-1:
                    dp[i][j] = arr[i][j]
                elif i == 0:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j+1])+arr[i][j]
                elif i == row-1:
                    dp[i][j] = max(dp[i-1][j+1],dp[i][j+1]) + arr[i][j]
                else:
                    maxa = [dp[i-1][j+1],dp[i][j+1],dp[i+1][j+1]]
                    dp[i][j] = max(maxa)+arr[i][j]
                    maxa = []
        for i in range(row):
            for j in range(col):
                print(dp[i][j],end = ",")
            print()
if __name__ == "__main__":
    arr = [[0,1,4,2,8,2],[4,3,6,5,0,4],[1,2,4,1,4,6],[2,0,7,3,2,2],[3,1,5,9,2,4],[2,7,0,8,5,1]]
    row = len(arr)
    col = len(arr[0])
    dp = [[-1 for j in range(col)]for i in range(row)]
    print(arr)
    print(solution().path(dp,arr,row,col))
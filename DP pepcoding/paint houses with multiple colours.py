class solution:
    def mincost(self,arr,dp):
        for i in range(len(dp[0])):
            dp[0][i] = arr[0][i]
        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                minn = float("inf")
                for k in range(len(dp[0])):
                    if k!=j:
                        if dp[i-1][k]<minn:
                            minn = dp[i-1][k]
                dp[i][j] = arr[i][j]+minn
        minn = float("inf")
        for i in range(len(dp[0])):
            if dp[len(dp)-1][i]<minn:
                minn = dp[len(dp)-1][i]
        return minn
    def mincostopt(self,arr,dp):
        least = float("inf")
        sleast = float("inf")
        for j in range(len(dp[0])):
            dp[0][j] = arr[0][j]
            if dp[0][j]<=least:
                sleast = least
                least = dp[0][j]
            elif dp[0][j]<sleast:
                sleast = dp[0][j]
        for i in range(1,len(dp)):
            nleast = float("inf")
            nsleast = float("inf")
            for j in range(len(dp[0])):
                if dp[i-1][j]==least:
                    dp[i][j] = arr[i][j]+sleast
                else:
                    dp[i][j] = arr[i][j]+least
                if dp[i][j]<=nleast:
                    nsleast = nleast
                    nleast = dp[i][j]
                elif dp[i][j]<nsleast:
                    nsleast = dp[i][j]
            least = nleast
            sleast = nsleast
        minn = float("inf")
        for j in range(len(dp[0])):
            if dp[(len(dp[0])-1)][j]<minn:
                minn = dp[(len(dp[0])-1)][j]
        return minn

if __name__ == "__main__":
    arr =  [[1, 2, 3],[11, 14, 5],[14, 3, 10]]
    dp = [[0 for j in range(len(arr[0]))]for i in range(len(arr))]
    print(solution().mincost(arr,dp))
    print(solution().mincostopt(arr,dp))
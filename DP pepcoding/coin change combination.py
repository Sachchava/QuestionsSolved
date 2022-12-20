class solution:
    def comb(self,dp,arr,amt):
        dp[0] = 1
        for i in range(len(arr)):
            for j in range(arr[i],len(dp)):
                dp[j]+=dp[j-arr[i]]
        return dp[amt]
if __name__ == "__main__":
    arr = [2,3,5,6]
    amt = 7
    dp = [0]*(amt+1)
    print(solution().comb(dp,arr,amt))
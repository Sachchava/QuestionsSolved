class solution:
    def permutation(self,dp,arr,amt):
        dp[0] = 1
        for i in range(1,len(dp)):
            for j in range(len(arr)):
                if i>=arr[j]:
                    dp[i] +=dp[i-arr[j]]
        return dp
if __name__ == "__main__":
    arr = [2,3,5,6]
    amt = 7
    dp = [0]*(amt+1)
    print(solution().permutation(dp,arr,amt))
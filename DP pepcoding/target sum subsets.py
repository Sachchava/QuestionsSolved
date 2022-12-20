class solution:
    def targetsum(self,dp,arr,target):
        for i in range(len(arr)+1):
            for j in range(target+1):
                if i == 0 and j ==0 :
                    dp[i][j] = True
                elif j ==0:
                    dp[i][j] = True
                elif i>0 and j>0:
                    if dp[i-1][j] == True:
                        dp[i][j] = True
                    else:
                        val = arr[i-1]
                        if dp[i][j-val]==True:
                            dp[i][j] = True
        for i in range(len(arr)+1):
            for j in range(target+1):
                print(dp[i][j],end = " ")
            print()

if __name__ == "__main__":
    n = 5
    arr = [4,2,7,1,3]
    target = 10
    dp = [[False for j in range(target+1)]for i in range(len(arr)+1)]
    print(dp)
    solution().targetsum(dp,arr,target)
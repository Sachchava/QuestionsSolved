class solution:
    def paths(self,n):
        if n==0:
            return 1
        elif n<0:
            return 0
        path1 = self.paths(n-1)
        path2 = self.paths(n-2)
        path3 = self.paths(n-3)
        # path4 = self.paths(n-4)
        pathn = path1 + path2 + path3
        return pathn
    def pathsmemorized(self,n,dp):
        if n == 0:
            return 1
        elif n<0:
            return 0
        if dp[n]>0:
            return dp[n]
        path1 = self.pathsmemorized(n-1,dp)
        path2 = self.pathsmemorized(n-2,dp)
        path3 = self.pathsmemorized(n-3,dp)
        pathn = path1 + path2 + path3
        dp[n] = pathn
        return pathn
    def pathstabulation(self,n,dp):
        dp[0] = 1
        for i in range(1,n+1):
            if i ==1:
                dp[i] = dp[i-1]
            elif i == 2:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
if __name__ =="__main__":
    print(solution().paths(5))
    dp = [0]*(5+1)
    print(solution().pathsmemorized(5,dp))
    dp = [0]*(5+1)
    print(solution().pathstabulation(5,dp))
class solution:
    def decode(self,strr):
        dp = [0]*(len(strr)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(dp)):
            if strr[i-1]<"0":
                dp[i] = dp[i-1]
            if strr[i-2] == "1" or strr[i-2]=="2" and strr[i-1] <="6":
                dp[i] += dp[i-2]
        return dp
if __name__ == "__main__":
    print(solution().decode("06"))
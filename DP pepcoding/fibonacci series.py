class solution:
    def fibo(self,num):
        if num==0 or num==1:
            return num
        fib1 = self.fibo(num-1)
        fib2 = self.fibo(num-2)
        fibn = fib1+fib2
        return fibn
    def fibmemoized(self,num,dp):
        if num==0 or num == 1:
            return num
        if dp[num]!=0:
            return dp[num]
        fib1 = self.fibmemoized(num-1,dp)
        fib2 = self.fibmemoized(num-2,dp)
        fibn = fib1 + fib2
        dp[num] = fibn 
        return fibn
if __name__ == "__main__":
    # print(solution().fibo(10))
    dp = [0]*(10+1)
    print(solution().fibmemoized(10,dp))
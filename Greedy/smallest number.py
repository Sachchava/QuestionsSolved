class Solution:
    def smallestNumber (self, s, m):
        if s>9*m:
            return -1
        res = []
        for i in range(m):
            res.append(0)
        s-=1
        for i in range(m-1,0,-1):
            if s>9:
                res[i]= 9
                s-=9
            else:
                res[i] = s
                s = 0
        print(s)
        res[0] = s+1
       
if __name__ == "__main__":
    s = 9
    d = 2
    Solution().smallestNumber(s,d)
class solution:
    def getperm(self,s,ans):
        if len(s)==0:
            print(ans,end = " ")
            return 
        for i in range(len(s)):
            ch = s[i]
            left = s[0:i]
            right = s[i+1:]
            self.getperm(left+right,ans+ch)
if __name__ == "__main__":
    solution().getperm("abc","")
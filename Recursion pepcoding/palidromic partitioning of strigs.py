class solution:
    def partition(self,s,asf):
        if len(s)==0:
            print(asf)
            return
        for i in range(len(s)):
            prefix = s[:i+1]
            ros = s[i+1:]
            if self.ispalindrome(prefix):
                self.partition(ros,asf + "(" + prefix + ")")
    def ispalindrome(self,s):
        lp = 0
        rp = len(s)-1
        while lp<rp:
            if s[lp]!=s[rp]:
                return False
            lp+=1
            rp-=1
        return True
if __name__== "__main__":
    s = "abaaba"
    solution().partition(s,"")
class solution:
    # dictionary = {}
    def dicttcheck(self,word):
        dictionary = {"rcbyn", "dy", "rcbyndy", "xx", "lorel"}
        return word in dictionary
    def wordbreak(self,str,n,ans,res): 
        for i in range(1,n+1):
            left = str[:i]
            if self.dicttcheck(left):
                if i==n:
                    ans += left
                    res.append(ans)
                    return 
                right = str[i:]
                self.wordbreak(right,len(right),ans+left+" ",res)
        return res
if __name__ == "__main__":
    str = "rcbyndyxxrcbyndyxx"
    res = []
    print(solution().wordbreak(str,len(str),"",res))
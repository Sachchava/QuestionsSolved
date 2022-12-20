class solution:
    def getsub(self,s,ans):
        if len(s)==0:
            print(ans)
            return
        left = s[:1]
        right = s[1:]
        self.getsub(right,ans+"")
        self.getsub(right,ans+left)
if __name__ == "__main__":
    (solution().getsub("abc",""))
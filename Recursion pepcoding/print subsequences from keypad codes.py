class solution:
    def comb(self,kpad,s):
        if len(s)==0:
            return [""]
        left = s[:1]
        right = s[1:]
        res = self.comb(kpad,right)
        ans = []
        l = kpad[int(left)]
        # print(l)
        for i in range(len(l)):
            for e in res:
                ans.append(l[i]+e)
        return ans
if __name__ == "__main__":
    kpad = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]
    s = "234"
    print(solution().comb(kpad,s))
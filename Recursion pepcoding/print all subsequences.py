class solution:
    def alls(self,s):
        if len(s)==0:
            return [""]
        left = s[:1]
        right = s[1:]
        res = self.alls(right)
        ans = []
        for e in res:
            ans.append(e+"")
            ans.append(e+left)
        # for w in res:
            # ans.append(w+left)
        return ans
if __name__ == "__main__":
    s = "abc"
    print(solution().alls(s) )      
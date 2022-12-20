class solution:
    def patternmatching(self,s,hmap,pattern,opattern):
        if len(pattern)==0:
            if len(s)==0:
                for e in hmap:
                    print(e,hmap[e])
            return
        firstch = pattern[0]
        remainingch = pattern[1:]
        if firstch not in hmap:
            for i in range(len(s)):
                left = s[:i+1]
                right = s[i+1:]
                hmap[firstch] = left
                self.patternmatching(right,hmap,remainingch,opattern)
                hmap.pop(firstch)
        else:
            lenn = len(hmap[firstch])
            prefix = s[:lenn]
            suffix = s[lenn:]
            if len(s)>=lenn:
                if prefix == hmap[firstch]:
                    self.patternmatching(suffix,hmap,remainingch,opattern)

if __name__ == "__main__":
    pattern = "pepe"
    s = "graphstreesgraphstrees"
    hmap = dict()
    solution().patternmatching(s,hmap,pattern,pattern)
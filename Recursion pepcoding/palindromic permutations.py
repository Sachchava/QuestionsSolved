class solution:
    def permutations(self,i,n,fmap,asf,oddc):
        if i>n:
            rev = ""
            for q in range(-1,-len(asf)-1,-1):
                rev+=asf[q]
            if oddc:
                asf+=oddc
            asf+=rev
            print(asf)
            return
        for e in fmap:
            freq = fmap.get(e)
            if freq>0:
                fmap[e] = fmap.get(e)-1
                self.permutations(i+1,n,fmap,asf+e,oddc)
                fmap[e] = freq
if __name__ == "__main__":
    s = "aaabb"
    s = sorted(s)
    fmap = dict()
    for e in s:
        if e not in fmap:
            fmap[e] = 0
        if e in fmap:
            fmap[e] = fmap.get(e)+1
    print(fmap)
    odd = 0
    oddc = ""
    lenn = 0
    for i in fmap:
        c = fmap.get(i)
        if c%2==1:
            odd+=1
            oddc = i
    for e in fmap:
        fmap[e] = int(c/2)
        lenn+=int(c/2)

    if odd >1 :
        print(-1)
    else:
        print(fmap,lenn)    

        solution().permutations(1,lenn,fmap, "",oddc)
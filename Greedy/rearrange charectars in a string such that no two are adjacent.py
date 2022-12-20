class solution:
    def rearrange(self,s):
        m = dict()
        
        # print(sorted(s))
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=1
            else:
                m[s[i]]+=1
        m = sorted(m.items(),key=lambda x: x[1],reverse=True)
        maxv= 0
        ss = 0
        for i in range(len(m)):
            if m[i][1]>maxv:
                maxv = m[i][1]
            ss+= m[i][1]
        print(m,ss,maxv)
        if abs(ss-maxv)==1:
            res = ""
            for i in range(len(m)):
                res+=m[i][0]
                
            return res
        else:
            print("not possible")
    
if __name__ == "__main__":
    s = "aab"
    print(solution().rearrange(s))
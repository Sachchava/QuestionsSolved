class solution:
    def value(self,s):
        dictt = dict()
        for i in range(len(s)):
            if s[i] not in dictt:
                dictt[s[i]]=1
            else:
                dictt[s[i]] = dictt.get(s[i],0)+1
        print(dictt)
        dictt = sorted(dictt.items(),key = lambda x:x[1],reverse = True)
        print(dictt)
        summ = (dictt[0][1]-k)*(dictt[0][1]-k)
        for i in range(1,len(dictt)):
            summ+=dictt[i][1]*dictt[i][1]
        return summ
if __name__ == "__main__":
    s =  "aaab"
    k = 2
    n = len(s)
    print(solution().value(s))
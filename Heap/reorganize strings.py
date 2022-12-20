class solution:
    def reorganize(self,s):
        dictt = dict()
        for i in range(len(s)):
            if s[i] not in dictt:
                dictt[s[i]] = 1
            else:
                dictt[s[i]] = dictt.get(s[i],0)+1
        dictt = list(sorted(dictt.items(),reverse = True, key = lambda items:items[1]))
        print(dictt)
        summ = 0
        for i in range(len(dictt)):
            summ+=dictt[i][1]
        print(summ)
        first = dictt[0][1]
        print(first)
        res = [0]*summ
        nsumm = summ-first
        i = 0
        j = 0
        if first == nsumm or first == nsumm+1 or first == nsumm-1:
            while dictt[j][1]!=0:
                res.insert(i,dictt[j][0])
                dictt[j][1]=dictt[j][1]-1
                i+=2
        print(res)
        
if __name__ == "__main__":
    s = 'bbbaa'
    (solution().reorganize(s))
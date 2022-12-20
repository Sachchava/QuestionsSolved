class solution:
    def solve(self,s1,s2,s3):
        dictt = dict()
        unique = ""
        num = [False for i in range(10)]
        for i in range(len(s1)):
            if s1[i] not in dictt:
                dictt[s1[i]]=-1
                unique+=s1[i]
        for i in range(len(s2)):
            if s2[i] not in dictt:
                dictt[s2[i]]=-1
                unique+=s2[i]
        for i in range(len(s3)):
            if s3[i] not in dictt:
                dictt[s3[i]]=-1
                unique+=s3[i]
        # for i in range(26):
        #    print(chr(ord('a')+i))
           
        self.mapper(s1,s2,s3,0,unique,dictt,num)
    def sumfinder(self,s,dictt):
        summ = 0
        for e in s:
            if e in dictt:
                summ+=dictt[e]
        return summ
    def mapper(self,s1,s2,s3,idx,unique,dictt,num):
        if idx==len(unique):
            sum1 = self.sumfinder(s1,dictt)
            sum2 = self.sumfinder(s2,dictt)
            sum3 = self.sumfinder(s3,dictt)
            if sum1+sum2 == sum3:
                print(sum1,sum2)
                print(sum3)
                for i in range(26):
                    alpha = chr(ord('a')+i)
                    if alpha in dictt:
                        print(alpha +":" +str(dictt[alpha]) ,end = " ")
                print()
            return 
        for i in range(10):
            if num[i]==False:
                dictt[unique[idx]] = i
                num[i] = True
                self.mapper(s1,s2,s3,idx+1,unique,dictt,num)
                dictt[unique[idx]] = -1
                num[i] = False


if __name__ == "__main__":
    s1 = "team"
    s2 = "pep"
    s3 = "toppr"
    solution().solve(s1,s2,s3)
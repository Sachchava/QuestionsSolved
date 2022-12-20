class solution:
    def survive(self,s,n,m):
        dum = s
        if int(dum/7)>0:
            dum-=int(dum/7)
        print(dum)
        foodwant = s*m
        print(foodwant)
        for i in range(dum):
            food = (i+1)*n
            if food>=foodwant:
                # print(i+1)
                return i+1
        return -1
        # print(foodwant)
        # if n*dum>=foodwant:
        #     print("will survive bcoz")
        #     print("he can buy"+ str(n*dum)+"foodpackets")
        #     print("and required food is "+str(foodwant))
        # else:
        #     print("wont survive bcoz")
        #     print("he can buy only "+ str(n*dum)+" foodpackets")
        #     print("and required food is "+str(foodwant))
if __name__ == '__main__':
    s = 27
    n = 27
    m = 2
    print(solution().survive(s,n,m))
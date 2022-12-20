class solution:
    def maxsum(self,ar):
        ar = sorted(ar)
        
        # return ar
        i = 0
        res = []
        route = True
        j = len(ar)-1
        while True:
            if route == True:
                res.append(ar[i])
                i+=1
                route = False
            elif route == False:
                res.append(ar[j])
                j-=1
                route = True
            if i>j:
                break
        s =0
        print(res)
        for i in range(len(ar)-1):
            s+=abs(res[i]-res[i+1])
        s+=abs(res[-1]-res[0])
        return s
            


if __name__ == "__main__":
    ar = [1, 2, 4, 8]
    print(solution().maxsum(ar))
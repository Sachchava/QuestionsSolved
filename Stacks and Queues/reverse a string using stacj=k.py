class solution:
    def reversee(self,a):
        res = ""
        for i in range(len(a)-1,-1,-1):
            res+=a[i]
        return res
    def reversee1(self,a):
        if len(a)==0:
            return 
        data = a[0]
        self.reversee1(a[1:])
        print(data,end = ' ')
if __name__ == "__main__":
    (solution().reversee1([1,2,3,4,5]))
class solution:
    def po1(self,n,x):
        if x==0 :
            return 1
        half = int(x//2)
        remains = int(x%2)
        if remains==1:
            return n*self.po1(n,half)*self.po1(n,half)
        else:
            return self.po1(n,half)*self.po1(n,half)

    def po(self,n,x):
        if x == 0:
            return 1
        return n*self.po(n,x-1)
if __name__ == "__main__":
    print(solution().po1(3,7))
    print(solution().po(3,7))
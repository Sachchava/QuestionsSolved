class solution:
    def findways(self,s,ans):
        if s<0:
            return 
        if s==0:
            print(ans,end = " ")
            return 
        self.findways(s-1,ans+"1")
        self.findways(s-2,ans+"2")
        self.findways(s-3,ans+"3")
if __name__ == "__main__":
    solution().findways(4,'')
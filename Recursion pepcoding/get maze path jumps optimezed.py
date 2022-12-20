class solution:
    def findpaths(self,pr,pc,dr,dc,ans):
        if pr==dr and pc==dc:
            print(ans,end = " ")
            return 
        i = 0
        while i<dc-pc:
            i+=1
            self.findpaths(pr,pc+i,dr,dc,ans+"h"+str(i))
        i = 0
        while i<dr-pr:
            i+=1
            self.findpaths(pr+i,pc,dr,dc,ans+"v"+str(i))
        i = 0
        while i<dc-pc and i<dr-pr:
            i+=1
            self.findpaths(pr+i,pc+i,dr,dc,ans+"d"+str(i))
if __name__ =="__main__":
    solution().findpaths(1,1,3,3,"") 
n = int(input())
m = int(input())

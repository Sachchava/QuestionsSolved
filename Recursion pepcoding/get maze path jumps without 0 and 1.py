class solution:
    def getjumps(self,pr,pc,dr,dc):
        if pr == dr and pc == dc:
            return [""]
        hor = []
        ver = []
        diag = []
        ans = []
        i = 0
        while i<dc-pc:
            i+=1
            hor = self.getjumps(pr,pc+i,dr,dc)
            
            for e in hor:
                ans.append(e+"h"+str(i))
            
        i = 0
        while i<dr-pr:
            i+=1
            ver = self.getjumps(pr+i,pc,dr,dc)
            
            for q in ver:
                ans.append(q+"v"+str(i))
                
            
        i = 0
        while i<dc-pc and i<dr-pr:
            i+=1
            diag = self.getjumps(pr+i,pc+i,dr,dc)
            for w in diag:
                ans.append(w+"d"+str(i))
            
        return ans  
if __name__ == "__main__":
    print(solution().getjumps(1,1,3,3))
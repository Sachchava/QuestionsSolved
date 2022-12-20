class solution:
    def path(self,pr,pc,dr,dc,ans):
        if pc == dc and pr == dr:
            print(ans,end = " ")
            return
        if pc<dc:
            self.path(pr,pc+1,dr,dc,ans+"h")
        if pr<dr:
            self.path(pr+1,pc,dr,dc,ans+"v")

if __name__ =="__main__":
    solution().path(1,1,3,3,"")
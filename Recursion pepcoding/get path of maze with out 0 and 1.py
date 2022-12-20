class solution:
    def getpath(self,pr,pc,dr,dc):
        if pr==dr and pc == dc:
            return [""]
        hor = []
        ver = []
        paths = []
        if pr<dr:
            hor = self.getpath(pr+1,pc,dr,dc)
        if pc<dc:
            ver = self.getpath(pr,pc+1,dr,dc)
        for e in hor:
            paths.append(e+"D")
        for j in ver:
            paths.append(j+"R")
        return paths

if __name__ == "__main__":
    print(solution().getpath(1,1,3,3))
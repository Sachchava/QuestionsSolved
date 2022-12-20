class solution:
    def order(self,l):
        for i in range(1,10):
            self.dfs(i,l)
    def dfs(self,j,l):
        if j>l:
            return
        print(j)
        for i in range(10):
            self.dfs(10*j+i,l)
if __name__ == "__main__":
    solution().order(100)
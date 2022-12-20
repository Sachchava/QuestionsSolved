class solution:
    def findpattern(self,chess,col,n):
        if col>=n:
            return True
        for i in range(n):
            if self.issafe(chess,i,col):
                chess[i][col]=1
                if self.findpattern(chess,col+1,n):
                    return True
                chess[i][col]=0
        return False
    def issafe(self,chess,row,col):
        for i in range(col):
            if chess[row][i]==1:
                return False
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if chess[i][j]==1:
                return False
        for i,j in zip(range(row,n,1),range(col,-1,-1)):
            if chess[row][col]==1:
                return False
        return True
if __name__ == "__main__":
    n = 4
    chess = [[0 for j in range(n)]for i in range(n)]
    solution().findpattern(chess,0,n)
    for i in chess:
        print(i)
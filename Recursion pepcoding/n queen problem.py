class solution:
    def narrangement(self,n):
        chess = [[0 for j in range(n)]for i in range(n)]
        self.nqueens(chess,0)
    def nqueens(self,chess,row):
        if row == len(chess):
            print(chess)
            return
        for col in range(len(chess)):
            if self.isqueensafe(chess,row,col)==True:
                chess[row][col]=1
                self.nqueens(chess,row+1)
                chess[row][col]=0
    def isqueensafe(self,chess,row,col):
        for i in range(0,row):
            if chess[i][col]==1:
                return False
        i = row
        j = col
        while i >= 0 and j >= 0:
            if(chess[i][j])==1:
                return False
            i -= 1
            j -= 1
    
        # Check lower diagonal on left side
        i = row
        j = col
        while i >= 0 and j < len(chess):
            if(chess[i][j])==1:
                return False
            i-=1
            j+=1
        return True
                

if __name__ == "__main__":
    # n = int(input("Enter N\n"))
    solution().narrangement(4)
class solution:
    def arrangement(self,n):
        board = [[ 0 for j in range(n)]for i in range(n)]
        cols = [0 for i in range(n)]
        lrdiag = [0 for i in range((2*n)-1)]
        rldiag = [0 for i in range((2*n)-1)]
        self.queensarr(n,0,board,cols,lrdiag,rldiag)
    def queensarr(self,n,row,board,cols,lrdiag,rldiag):
        if row == len(board):
            print(board)
            return 
        for columns in range(n):
            if cols[columns]==0 and lrdiag[row+columns]==0 and rldiag[row-columns+(len(board)-1)]==0:
                board[row][columns]=1
                cols[columns]=1
                lrdiag[row+columns]=1
                rldiag[row-columns+(len(board)-1)]=1
                self.queensarr(n,row+1,board,cols,lrdiag,rldiag)
                cols[columns]=0
                lrdiag[row+columns]=0
                rldiag[row-columns+(len(board)-1)]=0
                board[row][columns]=0
if __name__ == "__main__":
    solution().arrangement(4)
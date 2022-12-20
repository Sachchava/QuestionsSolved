class solution:
    def isvalid(self,board,row,col,pos):
        for i in range(len(board[0])):
            if board[row][i]==pos:
                return False
        for j in range(len(board)):
            if board[j][col]==pos:
                return False
        row1 = int(row/3)*3
        col1 = int(col/3)*3
        for i in range(3):
            for j in range(3):
                if board[row1+i][col1+j]==pos:
                    return False
        return True
    def solver(self,board,row,col):
        if row == len(board) :  
            print(board) 
            return board
        nrow = 0
        ncol = 0 
        if col==(len(board[0])-1):
            ncol = 0 
            nrow = row+1
        else:
            nrow = row
            ncol = col+1
        if board[row][col]!=0:
            self.solver(board,nrow,ncol)
        else:
            for i in range(1,10):
                if self.isvalid(board,row,col,i):
                    board[row][col]=i
                    self.solver(board,nrow,ncol)
                    board[row][col]=0  
        # return board/
if __name__ == "__main__":
    
    board = [[3,0,6,5,0,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1,],[0,0,3,0,1,0,0,8,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[1,3,0,0,0,0,2,5,0],[0,0,0,0,0,0,0,7,4],[0,0,5,2,0,6,3,0,0]]
    board1 = solution().solver(board,0,0)
    print(board1)
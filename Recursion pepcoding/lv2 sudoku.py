class solution:
    def solver(self,board,row,col):
        if row == len(board):
            self.display(board)
            return
        nrow = 0
        ncol = 0
        if col==len(board[0])-1:
            nrow=row+1
            ncol = 0
        else:
            nrow = row
            ncol=col+1
        if board[row][col]!=0:
            self.solver(board,nrow,ncol)
        else:
            for el in range(10):
                if self.validcheck(board,row,col,el):       
                    board[row][col]=el
                    self.solver(board,nrow,ncol)
                    board[row][col]=0
    def validcheck(self,board,row,col,pos):
        for i in range(len(board)):
            if board[i][col]==pos:
                return False
        for i in range(len(board[0])):
            if board[row][i]==pos:
                return False
        subr = int(row/3)*3
        subc = int(col/3)*3
        for i in range(3):
            for j in range(3):
                if board[subr+i][subc+j]==pos:
                    return False
        return True
    def display(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                print(arr[i][j],end = "")
            print()
if __name__ == "__main__":
    board = [[3,0,6,5,0,8,4,0,0],
[5,2,0,0,0,0,0,0,0],
[0,8,7,0,0,0,0,3,1],
[0,0,3,0,1,0,0,8,0],
[9,0,0,8,6,3,0,0,5],
[0,5,0,0,9,0,6,0,0],
[1,3,0,0,0,0,2,5,0],
[0,0,0,0,0,0,0,7,4],
[0,0,5,2,0,6,3,0,0]]
    solution().solver(board,0,0)
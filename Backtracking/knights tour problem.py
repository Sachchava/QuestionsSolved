class solution:
    def issafe(self,x,y,board):
        if x>=0 and y>=0 and x<n and y<n and board[x][y]==-1:\
            return True
        return False
    def printsol(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                print(arr[i][j],end='')
            print()
    def knightstour(self,n):
        board = [[-1 for j in range(n)]for i in range(n)]
        self.printsol(board)
        pos = 1
        board[0][0] = 0
        movex = [2, 1, -1, -2, -2, -1, 1, 2]
        movey = [1, 2, 2, 1, -1, -2, -2, -1]
        if self.pathfinder(n,movex,movey,0,0,board,pos):
            self.printsol(board)
            return
        else:
            print("no solution")
            return 
    def pathfinder(self,n,movex,movey,x,y,board,pos):
        # print(pos,n)
        if (pos==n*n):
            return True
        for i in range(n):
            x+=movex[i]
            y+=movey[i]
            if self.issafe(x,y,board):
                board[x][y]=pos
                if self.pathfinder(n,movex,movey,x,y,board,pos+1):
                    return True
                board[x][y]=-1
        return False
if __name__ == "__main__":
    n = 8
    solution().knightstour(8)
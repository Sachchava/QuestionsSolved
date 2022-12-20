class solution:
    def knightstour(self,chess,row,col,move):
        if row<0 or col<0 or row>=len(chess) or col>=len(chess) or chess[row][col]!=0:
            return 
        elif move == len(chess)*len(chess):
            chess[row][col]=move
            print(chess)
            chess[row][col]=0
            return 
        chess[row][col]=move
        self.knightstour(chess,row-2,col+1,move+1)
        self.knightstour(chess,row-1,col+2,move+1)
        self.knightstour(chess,row+1,col+2,move+1)
        self.knightstour(chess,row+2,col+1,move+1)
        self.knightstour(chess,row+2,col-1,move+1)
        self.knightstour(chess,row+1,col-2,move+1)
        self.knightstour(chess,row-1,col-2,move+1)
        self.knightstour(chess,row-2,col-1,move+1)
        chess[row][col]=0
if __name__ == "__main__":
    chess = [[0 for j in range(5)]for i in range(5)]
    solution().knightstour(chess,2,3,0)
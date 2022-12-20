class solution:
    def path(self,maze,row,col,visited,ans):
        if row == len(maze)-1 and col == len(maze[0])-1:
            print(ans)
            return
        if row<0 or row>len(maze)-1 or col<0 or col>len(maze[0])-1 or maze[row][col]==0 or visited[row][col]==True:
            return  
        visited[row][col]=True
        self.path(maze,row+1,col,visited,ans+"D")
        self.path(maze,row,col+1,visited,ans+"R")
        self.path(maze,row-1,col,visited,ans+"U")
        self.path(maze,row,col-1,visited,ans+"L")
        visited[row][col]=False
if __name__ == "__main__":
    maze = [ [1, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 1, 0, 1],
             [1, 1, 1, 1] ]
    visited = [[False for j in range(len(maze[0]))]for i in range(len(maze))]
    solution().path(maze,0,0,visited,"")
    
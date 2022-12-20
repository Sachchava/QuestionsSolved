class solution:
    def findpath(self,maze):
        path = ""
        allpaths = []
        visited = []
        for i in range(len(maze)):
            res = []
            for j in range(len(maze[0])):
                res.append(False)
            visited.append(res)
        self.pathfinder(0,0,maze,visited,path,allpaths)
        for q in allpaths:
            print(q)
    def pathfinder(self,row,col,maze,visited,path,allpaths):
        if (row == -1 or row == len(maze) or col == -1 or col == len(maze[0]) or visited[row][col] or maze[row][col]==0):
            return 
        if (row == len(maze)-1 and col==len(maze[0])-1 ):
            allpaths.append(path)
            return 
        visited[row][col]=True
        if self.issafe(row+1,col,visited,maze):
            path+="D"
            self.pathfinder(row+1,col,maze,visited,path,allpaths)
            # path=path[:-1]
        if self.issafe(row,col+1,visited,maze):
            path+="R"
            self.pathfinder(row,col+1,maze,visited,path,allpaths)
            # path=path[:-1]
        if self.issafe(row-1,col,visited,maze):
            path+="U"
            self.pathfinder(row-1,col,maze,visited,path,allpaths)
            # path=path[:-1]
        if self.issafe(row,col-1,visited,maze):
            path+="L"
            self.pathfinder(row,col-1,maze,visited,path,allpaths)
            # path=path[:-1]
        visited[row][col]=False
    def issafe(self,row,col,visited,maze):
        if (row == -1 or row == len(maze) or col == -1 or col == len(maze[0]) or visited[row][col] or maze[row][col]==0):
            return False
        return True
if __name__ == "__main__":
    maze = [ [1, 0, 0, 0],
             [1, 1, 1, 1],
             [1, 1, 0, 1],
             [1, 1, 1, 1] ]
    solution().findpath(maze)

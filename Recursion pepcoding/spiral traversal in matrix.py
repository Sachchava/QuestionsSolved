class solution:
    def spiraltraversal(self,arr,row,col,rl,cl):
        # if row<0 or col<0 or row>=len(arr) or col>=len(arr) or visited[row][col]!=0:
        #     return
        # if row>=0 and col>=0 and row<len(arr) and col<len(arr) and visited[row][col]==0:
        #     print(arr[row][col])
        #     visited[row][col]=1
        #     self.spiraltraversal(arr,visited,row,col+1)
        #     self.spiraltraversal(arr,visited,row+1,col)
        #     self.spiraltraversal(arr,visited,row,col-1)
        #     self.spiraltraversal(arr,visited,row-1,col)
        if row==(rl/2) and col == int(cl/2):
            return
        for i in range(cl):
            print(arr[row][i])
        for i in range(1,rl):
            print(arr[i][cl-1])
        for i in range(cl-2,col-1,-1):
            print(arr[rl-1][i])
        for i in range(rl-2,row,-1):
            print(arr[i][col])
        self.spiraltraversal(arr,row+1,col+1,rl,cl)
if __name__ == "__main__":
    arr = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    rl = len(arr)
    cl = len(arr[0])
    visited = [[0 for j in range(cl)]for i in range(rl)]
    solution().spiraltraversal(arr,0,0,rl,cl)
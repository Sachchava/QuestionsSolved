class solution:
    def sumfinder(self,arr,visited,bag):
        maxx = 0
        summ = 0
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr[row][col]!=0 and visited[row][col]!=True:
                    self.dfs(row,col,arr,visited,bag)
                    for e in bag:
                        summ+= e
                    if summ>maxx:
                        maxx = summ
        return maxx
    def dfs(self,row,col,arr,visited,bag):
        if row<0 or col<0 or row>=len(arr) or col>=len(arr[0]) or visited[row][col]==True or arr[row][col]==0:
            return 
        visited[row][col]=True
        bag.append(arr[row][col])
        self.dfs(row+1,col,arr,visited,bag)
        self.dfs(row,col+1,arr,visited,bag)
        self.dfs(row-1,col,arr,visited,bag)
        self.dfs(row,col-1,arr,visited,bag)
if __name__=="__main__":
    arr = [[0,1,4,2,8,2],[4,3,6,5,0,4],[1,2,4,1,4,6],[2,0,7,3,2,2],[3,1,5,9,2,4],[2,7,0,8,5,1]]
    visited = [[False for j in range(len(arr[0]))]for i in range(len(arr))]
    print(solution().sumfinder(arr,visited,[]))
class solution:
    def getdfs(self,adj,v):
        visited = [0 for i in range(v)]
        ans = []
        for i in range(v):
            if visited[i]==0:
                self.dfs(i,adj,ans,visited)
        return ans
    def dfs(self,node,adj,ans,visited):
        ans.append(node)
        visited[node]=1
        for j in range(len(adj[node])):
            if visited[j]==0:
                self.dfs(adj[node][j],adj,ans,visited)
if __name__ == "__main__":
    adj = [[1,2],[2,3],[0],[3]]
    v = len(adj)
    print(solution().getdfs(adj,v))
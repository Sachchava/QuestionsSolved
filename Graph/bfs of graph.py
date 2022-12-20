class solution:
    def bfs(self,adj,v):
        visited = [0 for i in range(v)]
        q = []
        ans = []
        for i in range(v):
            if visited[i]==0:
                q.append(i)
                visited[i]=1
                while q!=[]:
                    node = q.pop(0)
                    ans.append(node)
                    for j in range(len(adj[i])):
                        if visited[adj[i][j]]==0:
                            visited[adj[i][j]]=1
                            q.append(adj[i][j])
        return ans
if __name__ == "__main__":
    adj = [[2,5],[5,6,8],[],[4,5],[7],[7],[],[],[],[9]]
    v = len(adj)
    print(solution().bfs(adj,v))
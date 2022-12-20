class solution:
    def detect(self,start,visited,adj,v):
        q = [[start,-1]]
        visited[start]=1
        while q!=[]:
            node = q[0][0]
            prev = q[0][1]
            q.pop(0)
            for j in range(len(adj[start])):
                if visited[adj[start][j]]==0:
                    visited[adj[start][j]]=1
                    q.append([adj[start][j],node])
                elif prev!=adj[start][j]:
                    return True
        return False
    def detectcycle(self,adj,v):
        visited = [0 for i in range(v)]
        for i in range(v):
            if visited[i]==0:
                if self.detect(i,visited,adj,v):
                    return True
        return False
if __name__ == "__main__":
    adj = [[1],[2],[]]
    v = len(adj)
    print(solution().detectcycle(adj,v))
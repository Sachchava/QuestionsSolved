class adjnode:
    def __init__(self,data):
        self.vertex = data
        self.next = None
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None]*vertices
    def addnode(self,src,dest):
        node = adjnode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        node = adjnode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    def printgraph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            t = self.graph[i]
            while t:
                print("->{}".format(t.vertex),end = "")
                t = t.next
            print("\n")
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.addnode(0, 1)
    graph.addnode(0, 4)
    graph.addnode(1, 2)
    graph.addnode(1, 3)
    graph.addnode(1, 4)
    graph.addnode(2, 3)
    graph.addnode(3, 4)
 
    graph.printgraph()
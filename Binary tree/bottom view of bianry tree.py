class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def bottomview(self,root):
        if root ==None:
            return
        dic ={}
        mi = float('inf')
        q = [(root,0)]
        while len(q)>0:
            node = q.pop(0)
            if node[1] not in dic:
                dic[node[1]] = node[0].data
                mi= min(mi,node[1])
            if node[1] in dic:
                dic[node[1]] = node[0].data
            if node[0].left:
                q.append([node[0].left,node[1]-1])
            if node[0].right:
                q.append([node[0].right,node[1]+1 ])
        for i in dic:
            print(dic[mi])
            mi+=1
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    solution().bottomview(root)
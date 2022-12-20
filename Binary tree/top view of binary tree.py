class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def topview(self,root):
        dic = {}
        if root ==None:
            return 
        q = [(root,0)]
        mi = float('inf')
        while len(q)>0:
            node = q.pop(0)
            if node[1] not in dic:
                dic[node[1]]= node[0].data
                mi = min(mi,node[1])
            if node[0].left:
                q.append([node[0].left,node[1]-1])
            if node[0].right:
                q.append([node[0].right,node[1]+1])
        for i in dic:
            print(dic[mi])
            mi+=1
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    solution().topview(root)




  
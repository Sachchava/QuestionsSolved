class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def getverticalnodes(self,root,hodist,m):
        if root ==None:
            return 
        try:
            m[hodist].append(root.data)
        except:
            m[hodist]=[root.data]
        self.getverticalnodes(root.left,hodist-1,m)
        self.getverticalnodes(root.right,hodist+1,m)
    def verticaltraversal(self,root):
        m = dict()
        hodist = 0
        self.getverticalnodes(root,hodist,m)
        # for index,value in enumerate(sorted(m)):
        #     for i in m[value]:
        #         print(i)
        for i in sorted(m):
          print(m[i], end="")
    def verticalTraversal1(self, root):
        dic= []
        q = [(root,0)]
        mi = float('inf')
        res = []
        while len(q)>0:
            node = q.pop(0)
           
            dic.append([node[0].data,node[1]])
            if node[0].left :
                q.append([node[0].left,node[1]-1])
            if node[0].right:
                q.append([node[0].right,node[1]+1])
        print(dic)
        dic = sorted(dic,key = lambda c:c[1])
        print(dic)
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    # solution().vt(root)
    solution().verticaltraversal(root)
    solution().verticalTraversal1(root)

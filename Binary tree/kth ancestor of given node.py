class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def findancestor(self,a,k):
        if a==[]:
            return -1
        l = len(a)-k-1
        return a[l]


    def findpath(self,root,arr,x):
        if root == None:
            return 
        arr.append(root.data)
        if root.data == x:
            return arr
        if self.findpath(root.left,arr,x) or self.findpath(root.right,arr,x):
            return arr
        arr.pop()
        return False
    def kthnode(self,root):
        arr = []
        node = 4
        k = 2
        a = self.findpath(root,arr,node)
        return self.findancestor(a,k)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    print(solution().kthnode(root))
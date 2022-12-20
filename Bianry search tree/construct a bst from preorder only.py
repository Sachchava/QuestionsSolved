class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def constructor(self,preorder):
        self.ind = 0
        self.n = len(preorder)
        upperbound = float('inf')
        return self.treemaker(preorder,upperbound)
    def treemaker(self,preorder,upperbound):
        if self.ind>=self.n or preorder[self.ind] >=upperbound:
            return None
        node = Node(preorder[self.ind])
        self.ind+=1
        node.left = self.treemaker(preorder,node.data)
        node.right = self.treemaker(preorder,upperbound)
        return node
    def preorder(self,root,arr):
        if root == None:
            return None
        arr.append(root.data)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
        return arr
    def inorder(self,root):
        if root == None:
            return None
        
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left= Node(7)
    root.left.right = Node(9)
    root.right = Node(12)
    root.right.left = Node(11)
    root.right.right = Node(13)
    s = solution()
    arr = []
    p = s.preorder(root,arr)
    root1 = s.constructor(p)
    s.inorder(root1)


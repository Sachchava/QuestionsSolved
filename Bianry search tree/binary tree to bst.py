class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def preorder(self,root,arr):
        if root == None:
            return 
        arr.append(root.data)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
        return arr
    def bttobst(self,preorder):
        inorder = sorted(preorder)
        print(inorder)
        return self.buildbst(preorder,inorder)
    def buildbst(self,preorder,inorder):
        if len(inorder)==0:
            return None
        if len(preorder)==1:
            return Node(preorder[0])
        if len(inorder)==1:
            return Node(inorder[0])
        print(preorder[0])
        ind = inorder.index(preorder.pop(0))
        node = Node(inorder[ind])
        node.left = self.buildbst(preorder,inorder[:ind])
        node.right = self.buildbst(preorder,inorder[ind+1:])
        return node
    def inorder(self,root):
        if root==None:
            return None
        self.inorder(root.left)
        print(root.data,end = ' ')
        self.inorder(root.right)
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.left.right = Node(5)
    s = solution()
    arr = []
    pre = solution().preorder(root,arr)
    print(pre)
    root1 = solution().bttobst(pre)
    solution().inorder(root1)
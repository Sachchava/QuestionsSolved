class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def inorder(self,root,arr):
        if root == None:
            return 
        self.inorder(root.left,arr)
        arr.append(root.data)
        self.inorder(root.right,arr)
        return arr
    def buildbst(self,inorder):
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            return Node(inorder[0])
        ind = int(len(inorder)/2)
        node = Node(inorder[ind])
        node.left = self.buildbst(inorder[:ind])
        node.right = self.buildbst(inorder[ind+1:])
        return node
    def preorder(self,root):
        if root == None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)
    arr = []
    inor = solution().inorder(root,arr)
    root1 = solution().buildbst(inor)
    solution().preorder(root1)
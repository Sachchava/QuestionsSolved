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
    def preorder(self,root):
        if root == None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def levelorder(self,root):
        que = [root]
        while len(que)>0:
            node = que.pop(0)
            print(node.data)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
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
    def mergebst(self,root1,root2):
        a1 = []
        in1 = self.inorder(root1,a1)
        a2 = []
        in2 = self.inorder(root2,a2)
        # print(in1,in2)
        inn = in1+in2
        inn = sorted(inn)
        # print(inn)
        root = self.buildbst(inn)
        # self.preorder(root)
        print('level')
        a = []
        print(self.inorder(root,a))
if __name__ == '__main__':
    root1 = Node(8)
    root1.left = Node(5)
    root1.left.left = Node(3)
    root1.right = Node(9)
    root1.right.right = Node(14)
    root2 = Node(18)
    root2.left = Node(15)
    root2.left.left = Node(13)
    root2.right = Node(19)
    root2.right.right = Node(24)
    solution().mergebst(root1,root2)
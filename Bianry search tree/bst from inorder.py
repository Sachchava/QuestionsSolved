class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def buildbst(self,inorder):
        ind = int(len(inorder)/2)
        if len(inorder)==1:
            return Node(inorder[0])
        node = Node(inorder[ind])
        node.left = self.buildbst(inorder[:ind])
        node.right = self.buildbst(inorder[ind+1:])
        return node
    def levelorder(self,root):
        que = [root]
        while len(que)>0:
            node = que.pop(0)
            print(node.data)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
    def preorder(self,root):
        if root == None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
if __name__ == '__main__':
    inorder = [1,2,3,4,5,6,7]
    root = solution().buildbst(inorder)
    solution().levelorder(root)
    print('pre')
    solution().preorder(root)
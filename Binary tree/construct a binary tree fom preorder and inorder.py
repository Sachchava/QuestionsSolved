class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def build(self,preorder,inorder):
        if len(inorder)== 0:
            return None
        if len(preorder) == 1:
            return Node(preorder[0])
        ind = inorder.index(preorder.pop(0))
        node = Node(inorder[ind])
        node.left = self.build(preorder,inorder[:ind])
        node.right = self.build(preorder,inorder[ind+1:])
        return node
    def btpo(self,postorderr,inorder):
        if len(inorder)==0:
            return None
        if len(postorderr)==1:
            return Node(postorderr[0])
        ind = inorder.index(postorderr.pop(-1))
        node = Node(inorder[ind])
        node.left = self.btpo(postorderr,inorder[:ind])
        node.right = self.btpo(postorderr,inorder[ind+1:])
        return node
    def preorderr(self,root):
        if root == None:
            return 
        print(root.data)
        self.preorderr(root.left)
      
        self.preorderr(root.right)
        
    def postorder(self,root):
        if root == None:
            return 
      
        self.postorder(root.left)
      
        self.postorder(root.right)
        print(root.data)
if __name__ == '__main__':
    inorder = [1, 6, 8 ,7 ]
    preorder = [1, 6, 7, 8]
    postorderr = [8,7,6,1]
    root = solution().build(preorder,inorder)
    # solution().postorder(root)
    root1 = solution().btpo(postorderr,inorder)
    solution().preorderr(root1)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def postorder(self,root):
        if root == None:
            return 
      
        self.postorder(root.left)
      
        self.postorder(root.right)
        print(root.data)
    def treemaker(self,preorder,inorder):
        if len(inorder)==0:
            return None
        if len(preorder)==1:
            return Node(preorder[0])
        ind = inorder.index(preorder.pop(0))
        node = Node(inorder[ind])
        node.left =  self.treemaker(preorder,inorder[:ind])
        node.right = self.treemaker(preorder,inorder[ind+1:])
        return node
 
    def preorder(self,root,arr):
        if root == None:
            return None
        arr.append(root.data)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
        return arr
    def postorder1(self,root,arr):
        if root == None:
            return None
        
        self.postorder1(root.left,arr)
        self.postorder1(root.right,arr)
        arr.append(root.data)
        return arr
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
    # print(p)
    inorder = sorted(p)
    ansnode = s.treemaker(p,inorder)
    s.postorder(ansnode)
    arr1 = []
    print(s.postorder1(ansnode,arr1))
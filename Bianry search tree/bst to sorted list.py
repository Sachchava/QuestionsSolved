class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def bsttollist(self,root):
        dummy = Node(-1)
        self.curr = dummy
        self.inorder(root)
        self.curr.left = None
        self.curr.right = None
        return dummy.right
    def printll(self,root):
       
        while root!=None:
            print(root.data)
            root = root.right
    def preorder(self,root):
        if root == None:
            return 
     
        self.preorder(root.right)
        self.preorder(root.left)
        self.curr.right = root
        self.curr.left =  None
        self.curr = root
    def inorder(self,root):
        if root == None:
            return 
        self.inorder(root.left)
        self.curr.left = None
        self.curr.right = root
        self.curr = root
        self.inorder(root.right)
if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root1 = solution().bsttollist(root)
    solution().printll(root1)



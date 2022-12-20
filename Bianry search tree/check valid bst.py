class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def check(self,root):
        minv = float('-inf')
        maxv = float('inf')
        return self.validbst(root,minv,maxv)
    def validbst(self,root,minv,maxv):
        if root == None:
            return True
        if root.data > minv and root.data <maxv:
            #minv<root.data<maxv
            return self.validbst(root.left,minv,root.data) and self.validbst(root.right,root.data,maxv)
        return False
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left= Node(7)
    root.left.right = Node(9)
    root.right = Node(12)
    root.right.left = Node(11)
    root.right.right = Node(13)
    
    print(solution().check(root))
    # solution().inorder(root)
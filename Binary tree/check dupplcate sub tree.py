class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def preorder(self,root,s,n,m):
        if root == None:
            return 
        s = str(root.data)
        if root.left :
            s+= str(root.left.data)
            
        if root.right :
            s+= str(root.right.data)
            
        m.append(s)
        s = ""
        self.preorder(root.left,s,n,m)
        self.preorder(root.right,s,n,m)
        return m
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(4)
    root.right.left.right = Node(5)
    root.right.right = Node(7)
    s = ""
    n = ""
    m = []
    print(Solution().preorder(root,s,n,m))
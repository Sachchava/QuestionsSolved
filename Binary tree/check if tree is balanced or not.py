class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def h(self,root):
        if root == None:
            return 0
        return 1 + max(self.h(root.left),self.h(root.right))
    def isBalanced(self,root):
        if not root:
            return True
        lh = self.h(root.left)
        rh = self.h(root.right)
        if abs(lh-rh)<=1 and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True:
            return True
        return False
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.left.left.left = node(7)
if Solution().isBalanced(root):
    print("tree is balanced")
else:
    print("tree is not balanced")
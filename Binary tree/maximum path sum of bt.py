class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def findpath(self,root):
        if root == None:
            return 0
        l = max(0,self.findpath(root.left))
        r = max(0,self.findpath(root.right))
        self.ans = max(self.ans,root.data + l+r)
        return root.data + max(l,r)
    def maxsum(self,root):
        if not root:
            return 0
        self.ans = float('-inf')
        self.findpath(root)
        return self.ans
root = newNode(1)
root.left = newNode(-2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(-6)
root.right.right = newNode(2)
print(Solution().maxsum(root))
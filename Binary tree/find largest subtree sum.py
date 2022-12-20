class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def findtree(self,root):
        if root == None:
            return 0
        l = max(0,self.findtree(root.left))
        r = max(0,self.findtree(root.right))
        summ = root.data + l + r
        self.ans = max(self.ans,summ)
        return summ
    def maxsum(self,root):
        if root == None:
            return 0
        self.ans = float('-inf')
        self.findtree(root)
        return self.ans
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(-2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(-6)
    root.right.right = newNode(2)
    print(solution().maxsum(root))
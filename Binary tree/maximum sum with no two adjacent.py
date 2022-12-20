class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def maxsum(self,root):
        if root == None:
            return 0,0
        l = self.maxsum(root.left)
        r = self.maxsum(root.right)
        summ = l+r+root.data
        nsumm = l+r
        return summ,nsumm #not done
if __name__ == '__main__':
    root = newNode(10) 
    root.left = newNode(1) 
    root.left.left = newNode(2) 
    root.left.left.left = newNode(1) 
    root.left.right = newNode(3) 
    root.left.right.left = newNode(4) 
    root.left.right.right = newNode(5)
    print(solution().maxsum(root))
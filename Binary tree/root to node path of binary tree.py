class getNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def path(self,root,x,arr):
        if not root :
            return 
        arr.append(root.data)
        if root.data ==x:
            return True  
        if self.path(root.left,x,arr) or self.path(root.right,x,arr):
            return arr
        arr.pop()
        return False
if __name__ == '__main__':
    root = getNode(1)
    root.left = getNode(2)
    root.right = getNode(3)
    root.left.left = getNode(4)
    root.left.right = getNode(5)
    root.right.left = getNode(6)
    root.right.right = getNode(7)
    stack = []
    x = 4
    print(solution().path(root,x,stack))
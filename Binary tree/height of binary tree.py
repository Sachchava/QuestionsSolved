class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def height(root):
    if root == None:
        return 0
    lefth = height(root.left)
    righth = height(root.right)
    return 1+max(lefth,righth)
root = node(1)
root.left = node(2)
root.right  = node(3)
root.right.right = node(6)
root.right.left = node(7)
root.left.left = node(4)
root.left.right = node(5)
print(height(root))
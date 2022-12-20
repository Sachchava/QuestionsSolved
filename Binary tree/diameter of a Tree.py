class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))
def diameter(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    
    ld = diameter(root.left)
    rd = diameter(root.right)
    return max(lh + rh +1,max(ld,rd))
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(diameter(root))
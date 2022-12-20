class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def preorder(root):
    if root == None:
        return root

    print(root.data)
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root ==None:
        return root
    inorder(root.left)
    print(root.data)
    inorder(root.right)
def postorder(root):
    if root ==None:
        return root
    postorder(root.left)
    postorder(root.right)
    print(root.data)
# if '__name__'=='__main__':
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.right = node(6)
root.right.left = node(7)

# preorder(root)
inorder(root)
# postorder(root)
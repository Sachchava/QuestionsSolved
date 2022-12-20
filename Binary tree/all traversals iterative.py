class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def preorder(root):
    if root is None:
        return 
    stack = [root]
    ans = []
    while len(stack)>0:
        node = stack.pop()
        ans.append(node.data)
        print(node.data)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
def inorder(root):
    curr = root
    stack = []
    while True:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        
        if stack ==[]:
            break
        else :
            curr = stack.pop()
            print(curr.data)
            curr = curr.right
def postorder(root):
    s1 = [root]
    s2 = []
    while len(s1)>0:
        n = s1.pop()
        s2.append(n.data)
        if n.left is not None:
            s1.append(n.left)
        if n.right is not None:
            s1.append(n.right)
    while s2:
        g = s2.pop()
        print(g)
# def inorderUsingIteration(self, node):  # Iteration
#         print('')
#         while True:
#             while node is not None:
#                 self.stack.push(node)
#                 node = node.left
#             if self.stack.isEmpty():
#                 break
#             else:
#                 node = self.stack.pop()
#                 print(node.data, end=" ")
#                 node = node.right

root = node(1)
root.left = node(2)
root.right  = node(3)
root.right.left = node(7)
root.right.right = node(6)
root.left.left = node(4)
root.left.right = node(5)

# preorder(root)
# inorder(root)
postorder(root)
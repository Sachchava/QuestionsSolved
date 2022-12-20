class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def leafnodes(self,root):
        if root:
            self.leafnodes(root.left)
            if root.left ==None and root.right ==None:
                print(root.data)
            self.leafnodes(root.right)
            
    def leftsubtree(self,root):
        if root:
            if root.left:
                print(root.data)
                self.leftsubtree(root.left)
            elif root.right:
                print(root.data)
                self.leftsubtree(root.right)
    def rightsubtree(self,root):
        if root:
            if root.right:
                self.rightsubtree(root.right)
                print(root.data)
            elif root.left:
                self.rightsubtree(root.left)
                print(root.data)
       


    def boundarytraversal(self,root):
        if root:
            print(root.data)
            self.leftsubtree(root.left)
            self.leafnodes(root.left)
            self.leafnodes(root.right)
            self.rightsubtree(root.right)
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    solution().boundarytraversal(root)
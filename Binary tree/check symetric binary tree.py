class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def mirror(self,root1,root2):
        if root1 == None and root2 == None:
            return True

        if (root1.data == root2.data) or self.mirror(root1.left,root2.right) is True and self.mirror(root.right,root.left) is True:
            return True
        else:
            return False
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    root.right.right.right = Node(3)
    print(solution().mirror(root.left,root.right))
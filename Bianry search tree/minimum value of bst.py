class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def minv(self,root):
        # if root.left == None:
        #     return root.data
        while root.left:
            root = root.left
        return root.data
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(13)
    root.left.left = Node(6)
    root.left.right = Node(9)
    root.right.right = Node(15)
    root.right.left = Node(12)
    print(solution().minv(root))

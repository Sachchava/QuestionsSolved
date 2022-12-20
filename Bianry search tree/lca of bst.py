class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def lca(self,root,p,q):
        if max(p,q)<root.data:
            return self.lca(root.left,p,q)
        elif min(p,q)>root.data:
            return self.lca(root.right,p,q)
        else:
            return root.data
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left= Node(7)
    root.left.right = Node(9)
    root.right = Node(12)
    root.right.left = Node(11)
    root.right.right = Node(13)
    print(solution().lca(root,12,100))

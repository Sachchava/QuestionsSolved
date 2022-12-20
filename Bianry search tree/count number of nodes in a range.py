class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def count(self,root,l,h):
        if root == None:
            return 0
        curr = root.data
        if h>=curr and curr>=l:
            return 1 + self.count(root.left,l,h) + self.count(root.right,l,h)
        elif curr<l:
            return self.count(root.right,l,h)
        elif curr>h:
            return self.count(root.left,l,h)
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.left.left= Node(7)
    root.left.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(14)
    root.right.left = Node(11)
    print(solution().count(root,5,14))
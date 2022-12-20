class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def floor(self,root,x):
        s = float('-inf')
        p = float('inf')
        while root!=None:
           
            if root.data < x:
                s = max(s,root.data)
                root = root.right
                print('right')
            else:
                root = root.left
                print('left')
        return s
if __name__ == "__main__":
    root = Node(10)
    root.left= Node(8)
    root.left.right = Node(9)
    root.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(13)
    root.right.left = Node(11)
    x = 12
    print(solution().floor(root,x))

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def ceil(self,root,x):
        s = float('inf')
        
        while root!=None:
            # if root.data == x:
            #     return root.data
            if root.data > x:
                s = min(s,root.data)
                root = root.left
                print("left")
            else:
        
                root = root.right
                print("right")
        return s
if __name__ == '__main__':
    root = Node(10)
    root.left= Node(8)
    root.left.right = Node(9)
    root.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(13)
    root.right.left = Node(11)
    x = 12
    print(solution().ceil(root,x))
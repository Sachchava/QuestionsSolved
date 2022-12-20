class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def search(self,root,x):
        while root!=None :
            if root.data == x:
                return root.data
            if root.data< x:
                root = root.right
                print("right")
            else:
                root = root.left
                print("left")
        
if __name__ == '__main__':
    root = Node(10)
    root.left= Node(8)
    root.left.right = Node(9)
    root.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(13)
    root.right.left = Node(11)
    x = 113
    print(solution().search(root,x))
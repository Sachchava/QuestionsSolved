class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def successor(self,root,p):
    
        while root!=None:

            if root.data > x:
                s = root.data
                root = root.left
                print("left")
            else:
                root = root.right
                print("right")
        return s
    def predeccessor(self,root,p):
    
        while root!=None:

            if root.data > x:
            
                root = root.left
                print("left")
            else:
                p = root.data
                root = root.right
                print("right")
        return p
if __name__ == '__main__':
    root = Node(10)
    root.left= Node(8)
    root.left.right = Node(9)
    root.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(13)
    root.right.left = Node(11)
    x = 7   
    print(solution().successor(root,x))
    print(solution().predeccessor(root,x))
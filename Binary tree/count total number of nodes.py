class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def nodescount(self,root):
        if root == None:
            return 
        l = self.leftnodescount(root)
        r = self.rightnodescount(root)
        if l == r:
            return 2**r-1
        else:
            return 1+self.nodescount(root.left) + self.nodescount(root.right)
    def leftnodescount(self,root):
        count = 0
        while root:
            count+=1
            root = root.left
        return count
    def rightnodescount(self,root):
        count = 0
        while root:
            count+=1
            root = root.right
        return count
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(3) 
    root.right = Node(2)
    root.right.left = Node(4)
    root.right.right = Node(3)
    
    print(solution().nodescount(root))



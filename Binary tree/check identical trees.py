class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def identicalcheck(self,root1,root2):
        if root1 == None and root2== None:
            return True
        if root1!= None and root2!=None:
            if (root1.data == root2.data) and self.identicalcheck(root1.left,root2.left) and self.identicalcheck(root1.right,root2.right):
                return True
        return False

if __name__== '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    

    if solution().identicalcheck(root1,root2):
        print("trees are identical")
    else:
        print("trees are not identical")
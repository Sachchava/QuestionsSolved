class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def childrensum(self,root):
        if not root:
            return
        child = 0
        if root.left:
            child+=root.left.data
        if root.right:
            child+=root.right.data
        if child > root.data:
            root.data = child
        else:
            if root.right:
                root.right.data = root.data
            elif root.left:
                root.left.data = root.data
        self.childrensum(root.left)
        self.childrensum(root.left)
        total = 0
        if root.right:
            total+=root.right.data
        if root.left :
            total += root.left.data
           
        if root.right or root.left:
            root.data = total
           
        
    def levelorder(self,root):
        if root ==None:
            return
        arr = [root]
        while len(arr)>0:
            nod = arr.pop(0)
            print(nod.data)
            if nod.left:
                arr.append(nod.left)
            if nod.right:
                arr.append(nod.right)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right = Node(5)
    root.left.left = Node(4)
    solution().levelorder(root)
    r = solution().childrensum(root)
    solution().levelorder(r)

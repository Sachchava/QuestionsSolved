class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def morrisin(self,root,inorder):
        curr = root  
        while curr is not None:
            if curr.left is None:   
                inorder.append(curr.data)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right is not curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    inorder.append(curr.data)
                    curr = curr.right
        return inorder
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.left.left= Node(7)
    root.left.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(14)
    root.right.left = Node(11)
    for v in solution().morrisin(root,[]):
        print(v,end=" \n")
        
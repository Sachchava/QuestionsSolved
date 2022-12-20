class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def findnode(self,root,x):
        dummy = root
        if root == None:
            return None
        if root.data == x:
            return self.helper(root)
        while root!=None:
            if root.data >x:
                if root.left!=None and root.left.data == x:
                    root.left = self.helper(root.left)
                else:
                    root = root.left
            else:
                if root.right!=None and root.right.data == x:
                    root.right = self.helper(root.right)
                else:
                    root = root.right
        return dummy
    def helper(self,root):
        if root.right==None:
            return root.left
        elif root.left == None:
            return root.right
        else:
            rightchild = root.right
            curr = root.left
            while curr.right:
                curr = curr.right
            curr.right = rightchild
            return root.left
    def levelorder(self,root):
        s = [root]
        while len(s)>0:
            n = s.pop(0)
            print(n.data)
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
if __name__ == '__main__':
    root = Node(9)
    root.left = Node(8)
    root.left.left = Node(5)
    root.left.left.right = Node(7)
    root.left.left.right.left = Node(6)
    root.left.left.right.right = Node(8)
    root.left.left.left = Node(3)
    root.left.left.left.right = Node(4)
    root.left.left.left.left = Node(2)
    root.left.left.left.left.left = Node(1)
    
    root.right = Node(12)
    root.right.left = Node(10)
    root.right.left.right = Node(11)
    root.right.right = Node(13)
    x = 5
    root1 = solution().findnode(root,x)
    solution().levelorder(root1)
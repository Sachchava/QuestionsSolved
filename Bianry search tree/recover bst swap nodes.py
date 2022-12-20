class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def recover(self,root):
        first=middle=last= None
        prev = Node(float('-inf'))
        self.inorder(root,first,last,middle,prev)
        if first!=None and last!=None:

            first,last = last,first
        elif first!=None and middle!=None:
            first,middle = middle,first
        return root
    def inorder1(self,root):
        if root == None:
            return 
        self.inorder1(root.left)
        print(root.data)
        self.inorder1(root.right)

    def inorder(self,root,first,last,middle,prev):
        if root == None:
            return None
        self.inorder(root.left,first,last,middle,prev)
        if prev!=None and (root.data<prev.data):
            if first==None:
                first = prev
                middle = root
            else:
                last = root
        prev= root
        self.inorder(root.right,first,last,middle,prev)
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    root.right.left = Node(2)
    r = solution().recover(root)
    solution().inorder1(r)
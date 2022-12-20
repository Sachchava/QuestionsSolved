class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def stob(self,s):
        root = Node(ord(s[0])-ord('0'))
        stack = []
        for i in range(1,len(s)):
            if s[i] == "(":
                stack.append(root)
            elif s[i]==")":
                root = stack.pop()
            else:
                if root.left == None:
                    l = Node(ord(s[i])-ord('0'))
                    root.left = l
                    root= root.left
                elif root.right== None:
                    r = Node(ord(s[i])-ord('0'))
                    root.right = r
                    root = root.right
        return root
    def preorder(self,root):
        if root == None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
if __name__ == '__main__':
    s = "4(2(3)(1))(6(5))"
    r = solution().stob(s)
    solution().preorder(r)
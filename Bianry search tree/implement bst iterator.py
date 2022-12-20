class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def iterator(self,root):
        stack = []
        self.pushall(root,stack)
        return stack
    def next(self,stack):
        n = stack.pop()
        if n.right :
            self.pushall(n.right,stack)
        return n.data
    def pushall(self,root,stack):
        while root.left:
            stack.append(root.left)
            root = root.left
    def hasnext(self,stack):
        if stack==[]:
            return False
        return True
if __name__ == '__main__':
    root = Node(10)
    root.left= Node(8)
    root.left.right = Node(9)
    root.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(13)
    root.right.left = Node(11)
    s = solution()
    
    stack =s.iterator(root)
    print(s.next(stack))

 
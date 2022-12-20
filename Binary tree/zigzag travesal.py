class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution: 
    def zigzag(self,root):
        if root ==None:
            return 
        currlevel = [root]
        nextlevel = []
        ltr = True
        while len(currlevel)>0:
            temp = currlevel.pop()
            print(temp.data)
            if ltr:
                if temp.right:
                    nextlevel.append(temp.right)
                if temp.left:
                    nextlevel.append(temp.left)
            else:
                if temp.left:
                    nextlevel.append(temp.left)
                if temp.right:
                    nextlevel.append(temp.right)
            if len(currlevel)==0:
                ltr = not ltr
                currlevel,nextlevel = nextlevel,currlevel
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
            
    solution().zigzag(root)
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def toSumTree(self,root):
       
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return root.data
        oldval = root.data

        root.data = self.toSumTree(root.left)+self.toSumTree(root.right)+oldval
        return   root.data 
        # if root is None:
        #     return 0
        # old_value=root.data
        
        # l=self.toSumTree(root.left)
        # r=self.toSumTree(root.right)
        # old_value=root.data
        # root.data=l+r
        # return l+r+old_value
    def levelorder(self,root):
        s = [root]
        while len(s)>0:
            node = s.pop(0)
            print(node.data)
            if node.left :
                s.append(node.left)
            if node.right:
                s.append(node.right)
def Node(data) :
    temp = node(0)
    temp.data = data
    temp.left = None
    temp.right = None
     
    return temp
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    s = solution()
    # s.levelorder(root)
    s.toSumTree(root)
    s.levelorder(root)


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def checkdead(self,root,minv,maxv):
        if root == None:
            return False
        if minv == maxv:
            return True
        return self.checkdead(root.left,minv,root.data-1) or self.checkdead(root.right,root.data+1,maxv)
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    print(solution().checkdead(root,1,float('inf')))
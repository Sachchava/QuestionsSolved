class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
class solution:
    def preorder(self,root):
        if root == None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def updater(self,arr):
        mv = float('inf')
        
            
    def levelorder(self,root):
        que = [root]
        while len(que)>0:
            node = que.pop(0)
            print(node.data)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
if __name__ =='__main__':
    root = None
    s = solution()
    root = s.insert(root,10)
    root = s.insert(root,20)
    root = s.insert(root,30)
    root = s.insert(root,50)
    root = s.insert(root,60)
    root = s.insert(root,70)
    root = s.insert(root,100)
    s.levelorder(root)
    s.preorder(root)
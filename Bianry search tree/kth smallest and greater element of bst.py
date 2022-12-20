class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def kthsmall(self,root,k):
        if root == None:
            return None
        left = self.kthsmall(root.left,k)
        if left!=None:
            return left
        k-=1
        if k==0:
            return root.data
        return self.kthsmall(root.right,k)
    def kthlargest(self,root,k):
        n = self.nodes(root)
        k = n-k+1
        # print(k)
        return self.ikthsmall(root,k)

    def ikthsmall(self,root,k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            print(root.data)
            k-=1
            if k==0:
                return root.data
            # if root.right:
            root = root.right
    def nodes(self,root):
        if root == None:
            return 0
        return 1+self.nodes(root.right)+self.nodes(root.left)
    def inorder(self,root):
        if root == None:
            return 
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.left.left= Node(7)
    root.left.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(14)
    root.right.left = Node(11)
    print(solution().ikthsmall(root,4))
    # print(solution().nodes(root))
    # print(solution().kthlargest(root,1))
    # solution().inorder(root)
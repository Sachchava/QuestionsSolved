class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def bst(self,inorder):
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            return Node(inorder[0])
        ind = int(len(inorder)/2)
        node = Node(inorder[ind])
        node.left = self.bst(inorder[:ind])
        node.right = self.bst(inorder[ind+1:])
        return node
    def replacer(self,root,arr):
        res = []
        for i in range(len(arr)):
            node = root
            while root!=None:
                
                if root.data>arr[i]:
                    # print(arr[i],root.data)
                    succ = root.data
                    root = root.left
                else:
                    root = root.right
            res.append(succ)
            root = node
        return res
if __name__ == "__main__":
    arr = [ 8, 58, 71, 18, 31, 32, 63,
            92, 43, 3, 91, 93, 25, 80, 28 ]
    # print(arr)
    ino = sorted(arr)
    root1 = solution().bst(ino)
    # print(ino)
    print(solution().replacer(root1,arr))

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def insert(self,root,key):
        if root == None:
            return Node(key)
        curr = root
        while True:
            if root.data<key:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(key)
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(key)
                    break
        return curr
    def levelorder(self,root):
        que = [root]
        while len(que)>0:
            node = que.pop(0)
            print(node.data)
            if node.left :
                que.append(node.left)
            if node.right:
                que.append(node.right)
    def search(self,root,key):
        if key is None:
            return None
        while root:
            if root.data == key:
                return "Found"
            elif root.data > key:
                root = root.left
                print('left')
            else:
                root = root.right
                print("right")
        return "Node not present"
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(13)
    root.left.left = Node(6)
    root.left.right = Node(9)
    root.right.right = Node(15)
    root.right.left = Node(12)
    s = solution()
    root1 = s.insert(root,3)
    print(s.search(root1,3))
    # s.levelorder(root)
    # print("after")
    # s.levelorder(root1)

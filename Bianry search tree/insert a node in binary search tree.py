class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def insertt(self,root,x):
        if root == None:
            return Node(x)
        curr = root
        while True:
            if curr.data < x:
                if curr.right!=None:
                    print('right')
                    curr = curr.right
                else:
                    curr.right = Node(x)
                    break
            else:
                if curr.left != None:
                    print('left')
                    curr = curr.left
                else:
                    curr.left = Node(x)
                    break
        return root
    def preorder(self,root):
        if root == None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def levelorder(self,root):
        st = [root]
        while len(st)>0:
            node = st.pop(0)
            print(node.data)
            if node.left != None:
                st.append(node.left)
            if node.right!= None:
                st.append(node.right)
if __name__ == "__main__":
    root = Node(10)
    root.left= Node(8)
    root.left.right = Node(9)
    root.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(13)
    root.right.left = Node(11)
    x = 1
    root1 = solution().insertt(root,x)
    solution().preorder(root1)
    # solution().levelorder(root)
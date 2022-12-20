class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def reverselevelorder(root):
    queue =  [root]
    s = []
    while len(queue)>0:
        nod = queue.pop(0)
        s.append(nod.data)
        if nod.left !=None:
            queue.append(nod.left)
        if nod.right!=None:
            queue.append(nod.right)
    while s:
        print(s.pop())
root = node(1)
root.left = node(2)
root.right  = node(3)
root.right.left = node(7)
root.right.right = node(6)
root.left.left = node(4)
root.left.right = node(5)
reverselevelorder(root)

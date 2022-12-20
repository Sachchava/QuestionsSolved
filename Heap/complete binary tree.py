class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def complete(root,index,count):
    if root == None:
        return True
    if index>count:
        return False
    return (complete(root.left,((2*index)+1),count) and complete(root.right,((2*index)+2),count))
def countnodes(root):
    if root == None:
        return 0
    return 1+countnodes(root.left)+countnodes(root.right)
def checkmaxheap(root):
    if root.left is None and root.right is None:
        return True
    if root.right is None:
        return root.key>=root.left.key
    else:
        if root.key>=root.left.key and root.key>=root.right.key:
            return checkmaxheap(root.left) and checkmaxheap(root.right)
        else:
            return False
def heapcheck(root):
    count = countnodes(root)
    if checkmaxheap(root) and complete(root,0,count):
        print("binary tree is heap")
    else:
        print("binary tree is not heap")
if __name__ =="__main__":        
    root = Node(5)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(1)
    # index = 0
    # count = countnodes(root)
    heapcheck(root)

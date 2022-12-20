class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def isSumTree(node):
  
    # ls, rs

    # If node is None or it's a leaf 
    # node then return true
    if(node == None or
      (node.left == None and 
       node.right == None)):
        return 1

    # Get sum of nodes in left and 
    # right subtrees 
    ls = sum(node.left)
    rs = sum(node.right)

    # if the node and both of its children
    # satisfy the property return 1 else 0
    if((node.data == ls + rs) and 
        isSumTree(node.left) and 
        isSumTree(node.right)):
        return 1

    return 0

# Driver code
if __name__ == '__main__':
  
    root = Node(26)
    root.left= Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)
    
    if(isSumTree(root)):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")

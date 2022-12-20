from collections import defaultdict
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def levelorder(root):
    q = [root]
    while len(q)>0:
        nod = q.pop(0)
        print(nod.data)
        if nod.left !=None:
            q.append(nod.left)
        if nod.right !=None:
            q.append(nod.right)
def dfs(node, parent_node):
    if parent_node:
        adjacent_nodes[node.data].append(parent_node.data)
    if node.left:
        adjacent_nodes[node.data].append(node.left.data)
        dfs(node.left, node)
    if node.right:
        adjacent_nodes[node.data].append(node.right.data)
        dfs(node.right, node)
        

root = node(1)
root.left = node(2)
root.right  = node(3)
root.right.left = node(7)
root.right.right = node(6)
root.left.left = node(4)
root.left.right = node(5)
adjacent_nodes = defaultdict(list)
# levelorder(root)
dfs(root, None)
print(adjacent_nodes)
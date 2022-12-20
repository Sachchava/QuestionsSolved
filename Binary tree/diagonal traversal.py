
# A binary tree node


class Node:

	# Constructor to create a
	# new binary tree node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def diagonal(root):
    q = [(root,0)]
    m = []
    while len(q)>0:
        node = q.pop(0)
        m.append([node[0].data,node[1]])
        
        if node[0].left:
            q.append([node[0].left,node[1]+1])
        if node[0].right:
            q.append([node[0].right,node[1]])
    m = sorted(m,key = lambda x:x[1])
    for i in range(len(sorted(m))):
        print(m[i][0])
    
# Driver Code
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
diagonal(root)
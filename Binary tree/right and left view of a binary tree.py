class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def rightview(self,root):
        if root is None:
            return
        res = []
        q = [root]
        while len(q)>0:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level[-1])
        return res
    def leftview(self,root):
        if root is None:
            return
        res = []
        q = [root]
        while len(q)>0:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level[0])
        return res
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    print(solution().rightview(root))
    print(solution().leftview(root))

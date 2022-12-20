class Node:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None
class solution:
    def getpath(self,root,arr,x):
        if not root:
            return None
        arr.append(root.data)
        if root.data ==x :
            return arr
        if self.getpath(root.left,arr,x) or self.getpath(root.right , arr,x):
            return arr
        arr.pop()
        return False
    def ancestorcheck(self,arr1,arr2):
        
        if len(arr1)>len(arr2):
            for i in range(len(arr2)):
                if arr2[i]!=arr1[i]:
                    return arr2[i-1]
            return arr2[-1]
        else:
            for i in range(len(arr1)):
                if arr1[i]!=arr2[i]:
                    return arr1[i-1]
            return arr1[-1]

                   
    def commonancestor(self,root):
        arr1 = []
        arr2 = []
        x1 = 7
        x2 = 5
        a1 = self.getpath(root,arr1,x1)
        a2 = self.getpath(root,arr2,x2)
        a3 = self.ancestorcheck(a1,a2)
        return a3
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(solution().commonancestor(root))
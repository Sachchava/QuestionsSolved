class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def printvector(self,arr,i):
        for j in range(i,len(arr)):
            print(arr[j],end = '')
        print()
    def findnode(self,root,arr,k):
        if root == None:
            return 
        arr.append(root.data)
        self.findnode(root.left,arr,k)
        self.findnode(root.right,arr,k)
        s= 0
        for i in range(len(arr)-1,-1,-1):
            s+=arr[i]
            if s== k:
                self.printvector(arr,i)
        arr.pop()
    def sumpath(self,root,k):
        arr = []
        self.findnode(root,arr,k)

if __name__ == '__main__':
    
    root = newNode(1)
    root.left = newNode(3)
    root.left.left = newNode(2)
    root.left.right = newNode(1)
    root.left.right.left = newNode(1)
    root.right = newNode(-1)
    root.right.left = newNode(4)
    root.right.left.left = newNode(1)
    root.right.left.right = newNode(2)
    root.right.right = newNode(5)
    root.right.right.right = newNode(2)
    k = 5
    solution().sumpath(root,k)
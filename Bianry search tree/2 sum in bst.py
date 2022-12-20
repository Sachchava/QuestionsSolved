class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def inorder(self,root,arr):
        if root == None:
            return 
        self.inorder(root.left,arr)
        arr.append(root.data)
        self.inorder(root.right,arr)
        return arr
    def twosum(self,inorder,k):
        for i in range(len(inorder)):
            for j in range(i,len(inorder)):
                if inorder[i]+inorder[j]==k:
                    return inorder[i],inorder[j]
        return False
    def twosum1(self,inorder,k):
        p1,p2 = 0,len(inorder)-1
        while p2>p1:
            if inorder[p1]+inorder[p2] ==k:
                return inorder[p1],inorder[p2]
            elif inorder[p1]+inorder[p2]>k:
                p2 = p2-1
            elif inorder[p1]+inorder[p2] < k:
                p1 = p1+1
            else:
                return False
    def twosum2(self,inorder,k):
        for i in range(len(inorder)):
            x = k-inorder[i]
            l = len(inorder)
            low = 0
            high = l-1
            while high>low:
                mid = int((low+high)/2)
                if inorder[mid]==x:
                    return inorder[i],inorder[mid]
                elif inorder[mid]>x:
                    high = mid-1
                elif inorder[mid]<x:
                    low = low+1
    def twosum3(self,root,k,seen):
        if root == None:
            return None
        if k-root.data in seen:
            return k-root.data,root.data
        seen.add(root.data)
        return self.twosum3(root.left,k,seen) or self.twosum3(root.right,k,seen)
class bstiterator:
    stack = []
    stack1 = []
    def iterator(self,root):
        
        self.pushall(root,True)
    def iterator1(self,root):
        
        self.pushall(root,False)
    def pushall(self,root,bol):
        if bol == True:
            self.stack.append(root)
            while root.left:
                self.stack.append(root.left)
                root = root.left
        else:
            self.stack1.append(root)
            while root.right:
                self.stack1.append(root.right)
                root = root.right
    def next(self):
        
        node = self.stack.pop()
        if node.right:
            self.pushall(node.right,True)
        return node.data
    def prev(self):
        node = self.stack1.pop()
        if node.left:
            self.pushall(node.left,False)
        return node.data
    def twosum4(self,root,k):
        self.iterator1(root)
        self.iterator(root)
        i = self.next()
        j = self.prev()
        while j>i:
            if i+j==k:
                return i,j
            elif (i+j)>k:
                j = self.prev()
            else :
                i = self.next()
            

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.left.left= Node(7)
    root.left.left.left = Node(6)
    root.right = Node(12)
    root.right.right = Node(14)
    root.right.left = Node(11)
    # s = solution()
    # arr = []
    # k = 18
    # i = s.inorder(root,arr)
    # print(s.twosum(i,k))
    # print(s.twosum1(i,k))
    # print(s.twosum2(i,k))
    # print(s.twosum3(root,k,set()))
    print(bstiterator().twosum4(root,18))




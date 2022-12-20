class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class solution:
    def maxsum(self,root):
        if root == None:
            return 0
        return root.data + max(self.maxsum(root.left),self.maxsum(root.right))
    def sumfinder(self,root,l,s,maxlen,maxsum):
        if not root:
            if maxlen[0]<l:
                maxlen[0] = l
                maxsum[0] = s
            elif maxlen[0]==l and maxsum[0]<s:
                maxsum[0] = s
            return
        self.sumfinder(root.left,l+1,s+root.data,maxlen,maxsum)
        self.sumfinder(root.right,l+1,s+root.data,maxlen,maxsum)

    def maxsum1(self,root):
        if root == None:
            return 0
        maxlen = [0]
        maxsum = [-9999999999999]
        self.sumfinder(root,0,0,maxlen,maxsum)
        return maxsum[0]
if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.right.right = node(96)
    print(solution().maxsum1(root))
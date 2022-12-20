from heapq import heapify
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)
    return arr
def heapmaker(root,i,arr):
    if root is None:
        return 
    i[0]+=1
    root.data = arr[i[0]]
    heapmaker(root.left,i,arr)
    heapmaker(root.right,i,arr)
    
def bsttoheap(root):
    i = [-1]
    arr1 = []
    arr = inorder(root,arr1)
    print(arr)
    heapmaker(root,i,arr)
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    bsttoheap(root)
    a = []
    print(inorder(root,a))
   
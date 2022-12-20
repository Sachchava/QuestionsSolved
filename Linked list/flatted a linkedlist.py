def merge(l1,l2):
    temp = node(0)
    res = temp
    while l1!=None and l2!=None:
        if l1.data<l2.data:
            temp.bottom = l1.data
            l1 = l1.bottom
            temp = temp.bottom
        else:
            temp.bottom = l2.data
            l2 = l2.bottom
            temp = temp.bottom
        if l1 !=None:
            temp.bottom = l1
        else:
            temp.bottom = l2
    return res.bottom
def flatten(root):
    if root==None or root.next :
        return root
    root.next = flatten(root.next)
    root = merge(root,root.next)
    return root
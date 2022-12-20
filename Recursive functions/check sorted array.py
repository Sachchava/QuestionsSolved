def aa(a,ind):
    if ind>=len(a):
        return True
    if a[ind]<a[ind-1]:
        return False
    return aa(a,ind+1)
a = [1,2,45,3]
i = 1
print(aa(a,i))

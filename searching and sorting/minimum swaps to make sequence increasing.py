a = [0,3,5,8,9]
b = [2,1,4,6,9]
def aa(a,b):
    c= 0
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            c+=1
    for i in range(1,len(b)):
        if b[i]<b[i-1]:
            c+=1
    return c
print(aa(a,b))
a = [10,12]
b = [5,18,20]
def aa(a,b):
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i]>b[j]:
                a[i],b[j] = b[j],a[i]
    b = sorted(b)
    return(a,b)

print(aa(a,b))
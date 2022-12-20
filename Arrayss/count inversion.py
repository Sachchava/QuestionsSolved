a = [2,3,4,6,5]
b = []
def aa(a,b):
    for  i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                b.append([a[i],a[j]]) 
    return len(b)
print(aa(a,b))
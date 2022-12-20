def aaa(a,b,c):
    a = set(a)
    b = set(b)
    c= set(c)
    b.update(c,a)
    return len(b)
def aa(a,b,c):
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i] == b[j]:
                for k in range(0,len(c)):
                   if a[i] == c[k]:
                        return a[i]
            

a = [6,2]
b = [85,2,5,1,6,32,54]
c = [85,6]
print(aaa(a,b,c))
print(aa(a,b,c))
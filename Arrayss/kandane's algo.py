a = [1,2,-5,-7,4]
p = 0
m = -99999999999999
def aa(a,p,m):
    for i in range(0,len(a)):
        p = p + a[i]
        if p > m:
            m = p
        if p <= 0:
            p = 0
    return p
print(aa(a,p,m))
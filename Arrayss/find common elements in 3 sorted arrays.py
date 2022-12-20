a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]
d = []
def aa(a,b,c,d):
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            for k in range(len(c)):
                if a[i]==b[j]==c[k]:
                    d.append(a[i])
    return d
print(aa(a,b,c,d))
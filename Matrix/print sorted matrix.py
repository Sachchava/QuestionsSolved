a = [[1,5,3],[2,8,7],[4,6,9]]
b = []
c = []
for i in range(len(a)):
    for j in range(len(a[0])):
        b.append(a[i][j])
b = sorted(b)
for i in range(0,len(b),len(a[0])):
    r = []
    for j in range(i,i+len(a[0])):
        r.append(b[j])
    c.append(r)
print(a)
print(b)
print(c)

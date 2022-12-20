a = [[1], [2], [3]]
def aa(a):
    b = []
    r = len(a)
    c = len(a[0])
    for i in range(r):
        for j in range(c):
            b.append(a[i][j])
    b = sorted(b)
    low = 0
    high = len(b)
    mid = int((low+high)/2)
    return b[mid]

print(aa(a))
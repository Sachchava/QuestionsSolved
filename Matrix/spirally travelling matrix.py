
     #c1,r1
a =[[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]#rows,columns
rows = len(a)
columns = len(a[0])
c1 = 0
r1 = 0
b = []
tc = rows*columns
print(rows,columns,tc)
c = 0
def aa(a,b,r1,c1,rows,columns,c,tc):
    while c<=tc:
        if c==tc:
            return b
        else:
            for i in range(r1,rows):
                b.append(a[i][c1])
                c+=1
            c1+=1
        if c==tc:
            return b
        else:
            for i in range(c1,columns):
                b.append(a[rows-1][i])
                c+=1
            rows-=1
        if c==tc:
            return b
        else:
            for i in range(rows-1,r1-1,-1):
                b.append(a[i][columns-1])
                c+=1
            columns-=1
        if c==tc:
            return b
        else:
            for i in range(columns-1,c1-1,-1):
                b.append(a[r1][i])
                c+=1
            r1+=1
print(aa(a,b,r1,c1,rows,columns,c,tc))
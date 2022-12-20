def p(d,i,j):
    if i == d-1 and j== d-1:
        return 1
    if i>=d or j >=d:
        return 0
    return p(d,i+1,j)+p(d,i,j+1)
print(p(3,0,0))
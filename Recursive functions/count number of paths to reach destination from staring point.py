def c(s,e):
    if( s == e):
        return 1
    if (s>e):
        return 0
    count = 0
    for i in range(1,7):
        count+=c(s+i,e)
    return count
s = 0
e= 3
print(c(s,e))
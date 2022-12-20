a =[[1, 1], [0, 1]]
    
def bb(a,i):
    low = 0
    ans = len(a[0])
    ans1 = 0
    high = len(a[0])-1
    while low<=high:
        mid = int((low+high)/2)
        if a[i][mid]==1:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    ans1 = len(a[0])-ans
    return ans1
def aa(a):
    r = len(a)
    c = len(a[0])
    m = 0
    co = 0
    for i in range(r):
        c = bb(a,i)
        if c>m:
            m = c
            co = i
    return str(co) +" row contains " + str(m)+" ones's."

print(aa(a))
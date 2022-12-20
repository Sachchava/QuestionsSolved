def bb(a,mid):
    p = 1
    s = 0
    for i in range(len(a)):
        s+=a[i]
        if s>mid:
            s = a[i]
            p+=1
    return p

def aa(a,n):
    ma = 0
    sum = 0
    for i in range(len(a)):
        ma = max(ma,a[i])
        sum+a[i]
    low = 0
    high = sum
    while low<= high:
        mid = low+high/2
        v = bb(a,mid)
        if v<=n:
            high = mid
        else:
            low = mid+1
    return low
a = [10,20,30,40]
m = 2
print(aa(a,m))
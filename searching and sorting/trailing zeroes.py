n = 5
r = 0

def aa(mid,n):
    i = 5
    s = 0
    while i<=n:
        s+=mid//i
        i*=5
    if s>=n:
        return True
    return False

if n == 1:
    print("5")
else:
    low = 0
    high = 5*n
    ans = 0
    while low<= high:
        mid = low+high/2
        if aa(mid,n):
            ans = mid
            high = mid-1
        else:
            low = mid+1
print(low)

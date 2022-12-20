m = 7
a = [20,15,10,17]
ans = 0
low = 0
high = max(a)
def aa(a,m,mid):
    s = 0
    for i in range(len(a)):
    
        if a[i]>mid:
            s = s+ a[i]-mid
    if s>=m:
        return True
    else:
        return False
while low<=high:
    mid = (low+high)//2
    if aa(a,m,mid):
        ans = mid
        low = mid+1
   
    else:
        high = mid -1
print(ans)
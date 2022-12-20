a = [-1,-44,-47,-457,568,-4]
m = -999999999999
p = 0
def k(a,p,m):
    for i in range(0,len(a)):
        p = p + a[i]
        if p > m:
            m = p
        if p < 0:
            p = 0     
    if p == 0:
        p = max(a)
    return p
   

print(k(a,p,m))
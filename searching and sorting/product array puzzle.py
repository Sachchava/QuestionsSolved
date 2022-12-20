a = [-1,1,0,-3,3]
l = []
r = []
res = []
aa = 1
bb = 1
for i in range(len(a)):
    aa = a[i]*aa
    l.append(aa)
for i in range(-1,-len(a)-1,-1):
    bb = a[i]*bb
    r.append(bb)
r = r[::-1]



for i in range(len(a)):
    if i == 0:
        res.append(r[i+1])
    if i == len(a)-1:
        res.append(l[len(a)-2])
    if i !=0 and i!=len(a)-1:
        s = l[i-1]*r[i+1]
        res.append(s)
print(a,l,r,res)

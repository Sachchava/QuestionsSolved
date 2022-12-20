a = [[2,1,10],[3,1,40],[4,1,30],[1,4,20]]
a = sorted(a,key=lambda x:x[1],reverse = True)
m = a[0][1]
for i in range(len(a)):
    m = max(m,a[i][1])
b = [-1 for i in range(m)]

print(b,a)
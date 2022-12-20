a = [1,2,3,4,5,6,7]
a = sorted(a)
b = [3,5]
c = []
for i in range(0,len(a)):
    if a[i]<b[0]:
        c.append(a[i])
    if a[i]>= b[0] and a[i]<=b[1]:
        c.append(a[i])
    if a[i]>b[1]:
        c.append(a[i])
print(c)
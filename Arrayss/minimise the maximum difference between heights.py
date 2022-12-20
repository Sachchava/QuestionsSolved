a = [1,5,8,10]
k = 4
b = []
l = len(a)

for i in range(0,l):
    p = a[i] - k
    if p < 0:
        p = a[i] + k
        b.append(p)
        continue
    if p >= 0:
        b.append(p)
print(max(b)-min(b))
print(b)

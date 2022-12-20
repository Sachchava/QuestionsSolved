a = [1, 3, 5, 7]
b = [0, 2, 6, 8, 9]
if len(a) < len(b):
    for i in range(len(a)):
        if a[i] > b[0]:
            a[i],b[0]=b[0],a[i]
            b.sort()
else:
    for i in range(len(b)):
        if b[i] > a[0]:
            b[i],a[0]=a[0],b[i]
            a.sort()
print(a+b)
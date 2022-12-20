a = [2, 3, 5, 8]
b = [10, 12, 14, 16, 18, 20]
a.extend(b)
a = sorted(a)
l = int(len(a)/2)
if len(a)%2==0:
    m=int((a[l]+a[l-1])/2)
    print(m)
else:
    m = a[l]
    print(m)
a = [90 ,100, 78, 89, 67]
a = sorted(a)
l = int(len(a)/2)
if len(a)%2==0:
    m = (a[l]+a[l-1])/2
    print(int(m))
else:
    m = a[l]
    print(m)
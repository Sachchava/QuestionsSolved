a = [2, 2]
m = max(a)
b = []
for i in range(m):
    b.append(i)
for i in range(1,m):
    if b[i] not in a:
        print(str(b[i]) + str(" missing one"))
for i in range(m):
    if a[i] not in b:
        print(str(a[i]) + str(" repeated one"))
        break
a = [5, 2, 3, 9, 4, 6, 7, 15, 32]
r = []
for i in range(len(a)):
    b = bin(a[i])
    r.append(b)

print(sorted(r))
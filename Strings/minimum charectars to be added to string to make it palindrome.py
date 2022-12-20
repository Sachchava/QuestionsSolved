a = "ABCds"
c = 0
aa = a[::-1]
print(aa)
for i in range(len(aa)):
    d = aa[i:]
    if d!=d[::-1]:
        c+=1
    if d == d[::-1]:
        break
print(c)
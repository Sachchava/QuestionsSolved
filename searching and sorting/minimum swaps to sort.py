a = [10, 19, 6, 3, 5]
c = 0
d = 0
aa = sorted(a)
print(a,aa)
for i in range(len(a)):
    if a[i]!=aa[i]:
        c+=1
print(int((c/2)))
for i in range(len(a)):
    if a[i]==aa[i]:
        d+=1
        print(a[i],aa[i])
print(int((d/2)))
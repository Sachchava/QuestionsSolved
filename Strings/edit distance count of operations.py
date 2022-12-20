a = "sunday"
a = a.split()
print(a)
b = "saturday"
c = 0
for i in range(len(a)):
    if a[i] !=b[i]:
        if a[i] in b:
            ii = b.index(a[i])
            b.replace(b[i],b[ii])
        else:
            b.insert(a[i],i)
            b.pop(b[i+1])
    print(b)


a = [8,4,-10,10]
s = 0
for i in range(1,len(a)):
    aa = min(max(a[i::-1]),max(a[i:]))
    if a[i]<aa:
        s = s + aa - a[i]
print(s)
a =[5, 1, 3, 4, 7]
x = 12
s = []
c = 0
a = sorted(a)
for i in range(len(a)-2):
    j = i+1
    k = len(a)-1
    while j < k:
        b = []
        if a[i] + a[j] + a[k] < x:
            c += k -j
            b.append(a[i])
            b.append(a[j])
            b.append(a[k])
            s.append(b)
            j+=1
            
        else:
            k-=1
print(s,c)
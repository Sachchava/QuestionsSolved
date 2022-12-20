n = int(input("size of array"))
a = []
for i in range(n):
    a.append(int(input("enter values")))
q = int(input("enter bishu's power"))
s = []
ss = 0
a = sorted(a)
for i in range(len(a)):
    ss += a[i]
    s.append(ss)
print(a,s)
for i in range(len(a)):
    if a[i]==q :
        ii = a.index(a[i])
        print(a[i],s[ii])
    if q > a[len(a)-1]:
        iii = a.index(a[i])
        print(a[len(a)-1],s[len(a)-1])
        break
    if q < a[0]:
        
        print(a[0],s[0])
        break
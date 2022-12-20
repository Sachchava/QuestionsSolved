a = [1,9,3,10,4,20,2]
m = min(a)
a = sorted(a)
print(a)
s = 1
for i in range(0,len(a)):
    if a[i] == m+1 in a:
        s+=1
        m = a[i]
print(s)


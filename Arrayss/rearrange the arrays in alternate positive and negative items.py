a = [1, 2, 3, -4, -1, 4]
s = []
l = len(a)
a = sorted(a)
print(a)
i = 0
j = -1
if i%2==0 or i==0:
    s.append(a[i])
    i+=1
else:
    s.append(a[j])
    j-=1
    i+=1 
print(s)
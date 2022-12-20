a = [1, 4, 45, 6, 0, 19]
x = 51
q = []
for i in range(0,len(a)):
    p = 0
    c = 0
    for j in range(i,len(a)):
     p = p + a[j]
     c+=1
     if p > x:
         q.append(c)
print(min(q))

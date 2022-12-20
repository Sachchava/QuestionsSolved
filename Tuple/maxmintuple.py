t = (23,42,35,235,656,5,3,22)
t = sorted(t)
k = 2
l = len(t)
print(t)
for i in range(k):
    print(t[i],end=' ')
for j in range(-1,-k-1,-1):
    print(t[j],end=' ')    

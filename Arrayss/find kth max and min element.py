a = [4,23,235,23,513,6,2135,2,345,23]
k = 3
b = []
for i in range(0,len(a)):
    m = min(a)
    a.remove(m)
    b.append(m)
print(b)
print(b[k-1],b[-k])
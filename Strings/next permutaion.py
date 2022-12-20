a = [2,1,3]
p = []
for i in a:
    for j in a:
        for k in a:
            if i!=j and j!=k and k!=i:
                p.append([i,j,k])
for s in range(len(p)-1):
    if a==p[s]:
        print(p[s+1])
print(p)



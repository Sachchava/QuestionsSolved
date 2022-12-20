a = [[1,3],[2,6],[8,10],[15,18]]
b = []

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i][1]>a[j][0]:
            bb = [a[i][0],a[j][1]]
            b.append(bb)
        else:
            b.append(a[j])
            
print(b)
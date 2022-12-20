a = [5,5,10,100,10,5]
a1 = 0
a2 = 0
for i in range(0,len(a),2):
    a1 += a[i]
for j in range(1,len(a),2):
    a2 += a[j]
print(max(a1,a2))
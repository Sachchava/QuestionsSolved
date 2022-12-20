a = [6,-3,-10,0,2]
m = 0

for i in range(0,len(a)):
    p = 1
    for j in range(0,len(a)):
        p = p*a[j]
        if p > m:
            m = p
print(m)

        
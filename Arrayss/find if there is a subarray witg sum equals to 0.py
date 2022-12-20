a = [4,2,-1,1,6]
for i in range(0,len(a)):
    p = 0
    for j in range(i,len(a)):
        p = p + a[j]

        if p == 0:
            print(True)
            

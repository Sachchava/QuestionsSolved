q = 13
a = [1,4,45,6,10,8]
for i in range(len(a)):
    for j in  range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k]==q:
                print(True)
                print(a[i],a[j],a[k])
a = [3,1,2,2,1,2,3,3]
k = 4
s = int(len(a)/4)
for i in range(0,len(a)):
    c = 1
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            c+=1
            if c>s:
                print(a[i])
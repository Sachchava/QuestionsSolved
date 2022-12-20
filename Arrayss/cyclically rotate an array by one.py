a = [1,2,3,4,5]
l = len(a)
b = a[l-1]

for i in range(l-2,-1,-1):
    a[i+1] = a[i]
a[0]=b
print(a)    


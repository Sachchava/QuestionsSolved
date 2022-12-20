a = [1,2,3,4,5,6,6]
l = len(a)
def a(a,l):
    for i in range(0,l):
        for j in range(i+1,l):
            if a[i] == a[j]:
                return (a[i])
print(a(a,l))
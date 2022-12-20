a = [53,4,6,3,45,72,34,5,23]
l = len(a)
print(l)
if l == 1:
    max = a
    min = a
    print(max,min)
else:
    if a[0]<a[1]:
        max = a[1]
        min = a[0]
    else:
        min = a[1]
        max = a[0]

        for i in range(2,l):
            if a[i]>max:
                max = a[i]
            if a[i]<min:
                min = a[i]
        print(max,min)
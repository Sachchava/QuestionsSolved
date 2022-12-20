a = [5, 20, 3, 2, 5, 80]
x = 78
m = max(a)
for i in range(len(a)):
    if m-a[i]==x:
        print(m,a[i])
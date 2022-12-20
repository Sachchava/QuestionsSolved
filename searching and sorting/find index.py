a = [4, 5, 6, 7, 6]
x = 9
for i in range(len(a)):
    if a[i] == x:
        print(i)
        break
if x not in a:
    print(False)
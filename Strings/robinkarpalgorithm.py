a = "CAADAABAABA"
a = a.lower()
b = "aaba"
bl = len(b)
for i in range(len(a)):
    if a[i:i+bl] == b:
        print(i)
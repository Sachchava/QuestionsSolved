a = "abc"
for i in range(len(a)):
    k = ""
    for j in range(i,len(a)):
        k = a[j] +k
        print(k)
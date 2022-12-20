a = ["act","god","cat","dog","tac"]
b = []
c = []
for i in range(len(a)):
    for j in range(i,len(a)):
        if sorted(a[i])==sorted(a[j]):
            if a[j] not in b:
                b.append(a[j])
print(b)
a = [1,5,7,1]
s = 6
c = 0
def aa(a,s,c):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i] + a[j] == s:
                c+=1
    return c
print(aa(a,s,c))
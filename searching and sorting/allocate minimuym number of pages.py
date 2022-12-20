a = [12,34,67,90]
s = 0
a1 = []
a2 = []
m= [] 
for i in range(len(a)):
    s =s +a[i]
    a1.append(s)
s = 0
for i in range(-1,-len(a)-1,-1):
    s+=a[i]
    a2.append(s)
a2 = a2[::-1]
for i in range(len(a)-1):
    if a1[i] > a2[i+1]:
        m.append(a1[i])
    else:
        m.append(a2[i+1])
print(a)
print(a1)
print(a2)
print(min(m))
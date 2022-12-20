a = "0111100010"
c = 0
o = 0
z = 0

for i in range(len(a)):
    if a[i] == "0":
        z+=1
    else:
        o+=1
    if o==z:
        c+=1
if c == 0:
    print("-1")
else:
    print(c)